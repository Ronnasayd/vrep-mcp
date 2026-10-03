"""Semantic search over the catalog with a hash-keyed on-disk embedding cache."""

from __future__ import annotations

import hashlib
import os
import re
from functools import lru_cache
from pathlib import Path
from typing import Any

import numpy as np

from . import catalog

MODEL_ID = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
KINDS = ("function", "constant")
MIN_RESULTS, MAX_RESULTS = 1, 50
DESCRIPTION_LIMIT = 200
HASH_PREFIX_LEN = 16
# invariant: bump when the indexed text format changes so stale caches are not reused
TEXT_FORMAT_VERSION = "camel-split-v1"
_CAMEL_BOUNDARY = re.compile(r"(?<=[a-z])(?=[A-Z])")


@lru_cache(maxsize=1)
def _embedder() -> Any:
    # invariant: lazy import and construction (OPS-03); importing this module must stay cheap
    from fastembed import TextEmbedding

    return TextEmbedding(MODEL_ID)


def _cache_path(catalog_hash: str) -> Path:
    cache_dir = Path(
        os.environ.get("VREP_CACHE_DIR", Path.home() / ".cache" / "vrep-mcp")
    )
    key = hashlib.sha256(f"{catalog_hash}:{TEXT_FORMAT_VERSION}".encode()).hexdigest()
    return cache_dir / f"index-{key[:HASH_PREFIX_LEN]}.npy"


def _embed(texts: list[str]) -> np.ndarray:
    vectors = np.asarray(list(_embedder().embed(texts)), dtype=np.float32)
    return vectors / np.linalg.norm(vectors, axis=1, keepdims=True)


def _build(path: Path) -> np.ndarray:
    entries = catalog.entries()
    # why: split names rank multilingual queries higher (SRCH-05 was 7th with raw names)
    vectors = _embed(
        [
            f"{_CAMEL_BOUNDARY.sub(' ', n)}: {entries[n]['description']}"
            for n in sorted(entries)
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    # hazard: write-then-rename so a concurrent process never loads a half-written file
    tmp = path.with_suffix(".tmp.npy")
    np.save(tmp, vectors)
    os.replace(tmp, path)
    return vectors


@lru_cache(maxsize=1)
def _vectors_for(catalog_hash: str) -> np.ndarray:
    path = _cache_path(catalog_hash)
    return np.load(path) if path.exists() else _build(path)


def _validate(
    query: str, max_results: int, namespace: str | None, kind: str | None
) -> None:
    if not query.strip():
        raise catalog.VrepError("query must not be empty")
    if not MIN_RESULTS <= max_results <= MAX_RESULTS:
        raise catalog.VrepError(
            f"max_results must be between {MIN_RESULTS} and {MAX_RESULTS}"
        )
    if namespace is not None and namespace not in catalog.NAMESPACES:
        raise catalog.VrepError(
            f"Unknown namespace '{namespace}'. Valid: {', '.join(catalog.NAMESPACES)}"
        )
    if kind is not None and kind not in KINDS:
        raise catalog.VrepError("kind must be 'function' or 'constant'")


def _scores(query: str) -> np.ndarray:
    try:
        vectors = _vectors_for(catalog.catalog_hash())
        return vectors @ _embed([query])[0]
    except catalog.VrepError:
        raise
    except Exception as exc:
        raise catalog.VrepError(f"Search index unavailable: {exc}") from exc


def search(
    query: str,
    max_results: int = 10,
    namespace: str | None = None,
    kind: str | None = None,
) -> list[dict[str, Any]]:
    _validate(query, max_results, namespace, kind)
    entries = catalog.entries()
    scores = _scores(query)
    rows = []
    for name, score in zip(sorted(entries), scores):
        e = entries[name]
        if (namespace and e["namespace"] != namespace) or (kind and e["kind"] != kind):
            continue
        rows.append(
            {
                "name": name,
                "kind": e["kind"],
                "namespace": e["namespace"],
                "description": e["description"][:DESCRIPTION_LIMIT],
                # invariant: SRCH-01 range is 0-100, so negative cosine clamps to 0
                "score": round(max(0.0, float(score)) * 100, 2),
            }
        )
    rows.sort(key=lambda r: (-r["score"], r["name"]))
    return rows[:max_results]
