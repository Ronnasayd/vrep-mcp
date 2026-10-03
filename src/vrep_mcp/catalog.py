"""Catalog of CoppeliaSim API functions/constants, built from processed/*.json."""

from __future__ import annotations

import base64
import hashlib
import json
import os
import re
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable

NAMESPACES = ("sim", "simUI", "simROS2", "simVision")
_FILES = tuple(f"{ns}.json" for ns in NAMESPACES) + ("constants.json",)
_JSON_TYPES = {
    "int": "integer",
    "float": "number",
    "string": "string",
    "bool": "boolean",
    "list": "array",
    "float[]": "array",
    "int[]": "array",
    "dict": "object",
    "map": "object",
}


class VrepError(Exception):
    """Domain error; server.py maps it to an MCP tool error."""


def _data_dir() -> Path:
    return Path(
        os.environ.get("VREP_DATA_DIR", Path(__file__).parents[2] / "processed")
    )


def _read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError) as exc:
        raise VrepError(f"Catalog file {path} missing or invalid: {exc}") from exc


@lru_cache(maxsize=4)
def _load(data_dir: Path) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for ns in NAMESPACES:
        for m in _read_json(data_dir / f"{ns}.json"):
            out[f"{ns}.{m['method']}"] = _normalize(ns, m)
    # invariant: constants.json carries no prefix; they all live in `sim`
    for c in _read_json(data_dir / "constants.json"):
        name, _, typ = c["constant"].partition(":")
        out[f"sim.{name}"] = {
            "name": f"sim.{name}",
            "kind": "constant",
            "namespace": "sim",
            "method": name,
            "type": typ,
            "signature": "",
            "params": [],
            "param_docs": [],
            "returns": [],
            "url": None,
            "description": f"Constant sim.{name} ({typ})",
        }
    return out


def _normalize(ns: str, m: dict[str, Any]) -> dict[str, Any]:
    # CAT-07: entries without python_raw only have lua data
    src, raw = (
        (m["python"], m["python_raw"])
        if m.get("python_raw")
        else (m["lua"], m.get("lua_raw") or "")
    )
    params = src["params"]
    defs = m.get("params_definitions") or []
    # invariant: params_definitions aligns with params only when lengths match (CAT-06)
    return {
        "name": f"{ns}.{m['method']}",
        "kind": "function",
        "namespace": ns,
        "method": m["method"],
        "description": (m.get("description") or "").strip(),
        "url": m.get("url"),
        "signature": raw,
        "params": params,
        "param_docs": [d.strip() for d in defs] if len(defs) == len(params) else [],
        "returns": src["returns"],
        "type": None,
    }


def entries() -> dict[str, dict[str, Any]]:
    """Map 'sim.getObject' -> normalized entry. Raises VrepError on a bad catalog file."""
    return _load(_data_dir())


def get(name: str) -> dict[str, Any]:
    e = entries().get(name)
    if e is None:
        raise VrepError(f"Unknown function '{name}'. Use search_functions.")
    return e


def catalog_hash() -> str:
    h = hashlib.sha256()
    for f in sorted(_FILES):
        path = _data_dir() / f
        try:
            h.update(path.read_bytes())
        except OSError as exc:
            raise VrepError(f"Catalog file {path} missing or invalid: {exc}") from exc
    return h.hexdigest()


def list_namespaces() -> list[dict[str, Any]]:
    es = entries().values()
    return [
        {
            "namespace": ns,
            "functions": sum(
                e["namespace"] == ns and e["kind"] == "function" for e in es
            ),
            "constants": sum(
                e["namespace"] == ns and e["kind"] == "constant" for e in es
            ),
        }
        for ns in NAMESPACES
    ]


def _words(s: str) -> set[str]:
    return {w.lower() for w in re.findall(r"[A-Za-z][a-z0-9]*|[A-Z]+(?![a-z])", s)}


def search(
    query: str, max_results: int = 10, namespace: str | None = None
) -> list[dict[str, Any]]:
    q = _words(query) | {query.lower()}
    scored = []
    for name, e in entries().items():
        if namespace and e["namespace"] != namespace:
            continue
        nl, desc = name.lower(), e.get("description", "").lower()
        score = sum(3 * (w in nl) + (w in desc) for w in q if w) + 5 * (
            query.lower() == nl
        )
        if score:
            scored.append((score, name, e))
    scored.sort(key=lambda t: (-t[0], t[1]))
    return [
        {
            "name": n,
            "kind": e["kind"],
            "score": s,
            "description": e.get("description", "")[:200].strip(),
        }
        for s, n, e in scored[:max_results]
    ]


def _is_optional(e: dict[str, Any], pname: str) -> bool:
    return bool(re.search(rf"\b{re.escape(pname)}\s*=", e["signature"]))


def schema(name: str) -> dict[str, Any]:
    e = get(name)
    if e["kind"] == "constant":
        return {
            "name": name,
            "kind": "constant",
            "namespace": e["namespace"],
            "type": e["type"],
        }
    props = {}
    for i, p in enumerate(e["params"]):
        prop = {"x-vrep-type": p["param_type"]}
        if p["param_type"] in _JSON_TYPES:
            prop["type"] = _JSON_TYPES[p["param_type"]]
        if e["param_docs"]:
            prop["description"] = e["param_docs"][i]
        props[p["param_name"]] = prop
    return {
        "name": name,
        "kind": "function",
        "namespace": e["namespace"],
        "signature": e["signature"],
        "description": e["description"],
        "url": e["url"],
        "returns": e["returns"],
        "inputSchema": {
            "type": "object",
            "properties": props,
            "required": [n for n in props if not _is_optional(e, n)],
        },
    }


# bool is a subclass of int: listed types exclude it explicitly in _json_type
_PY_TYPES = {
    "integer": int,
    "number": (int, float),
    "string": str,
    "boolean": bool,
    "array": list,
    "object": dict,
}


def _json_type(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    return next(
        (t for t, py in _PY_TYPES.items() if t != "number" and isinstance(value, py)),
        type(value).__name__,
    )


def _type_ok(expected: str, value: Any) -> bool:
    if isinstance(value, bool):
        return expected == "boolean"
    return value is not None and isinstance(value, _PY_TYPES[expected])


def to_positional(name: str, arguments: dict[str, Any]) -> list[Any]:
    """Named args -> positional list (ZMQ API is positional), truncated after the last given one."""
    s = schema(name)
    props, required = s["inputSchema"]["properties"], s["inputSchema"]["required"]
    missing = [r for r in required if r not in arguments]
    if missing:
        raise VrepError(f"Missing required argument(s): {missing}")
    unknown = sorted(set(arguments) - set(props))
    if unknown:
        raise VrepError(f"Unknown argument(s) {unknown}; expected {list(props)}")
    last = max((i for i, p in enumerate(props) if p in arguments), default=-1)
    gaps = [p for i, p in enumerate(props) if i < last and p not in arguments]
    if gaps:
        raise VrepError(
            f"Optional argument(s) {gaps} must be given because a later one is set"
        )
    for p, prop in props.items():
        if (
            p in arguments
            and "type" in prop
            and not _type_ok(prop["type"], arguments[p])
        ):
            raise VrepError(
                f"Argument '{p}' expected {prop['type']}, got {_json_type(arguments[p])}"
            )
    return [arguments[p] for i, p in enumerate(props) if i <= last]


def jsonable(v: Any) -> Any:
    return json.loads(
        json.dumps(
            v,
            default=lambda o: (
                base64.b64encode(o).decode()
                if isinstance(o, (bytes, bytearray))
                else repr(o)
            ),
        )
    )


_client = None


def _api(ns: str) -> Any:
    global _client
    if _client is None:
        from coppeliasim_zmqremoteapi_client import RemoteAPIClient

        _client = RemoteAPIClient(
            os.environ.get("VREP_HOST", "localhost"),
            int(os.environ.get("VREP_PORT", "23000")),
        )
    return _client.require(ns)


def call(
    name: str, arguments: dict[str, Any] | None = None, api: Callable[[str], Any] = _api
) -> Any:
    e = get(name)
    obj = api(e["namespace"])
    if e["kind"] == "constant":
        return jsonable(getattr(obj, e["method"]))
    return jsonable(getattr(obj, e["method"])(*to_positional(name, arguments or {})))
