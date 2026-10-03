import importlib
import re
import zlib

import numpy as np
import pytest

from vrep_mcp import catalog, index

DIM = 8192


class FakeEmbedder:
    """Hashed bag of words: texts sharing words get a high cosine."""

    def __init__(self):
        self.calls = []

    def embed(self, texts):
        self.calls.append(list(texts))
        for text in texts:
            vec = np.zeros(DIM, dtype=np.float32)
            for word in re.findall(r"[a-z0-9]+", text.lower()):
                vec[zlib.crc32(word.encode()) % DIM] += 1.0
            yield vec


class AxisEmbedder:
    """Documents point along +x; the query word picks the direction."""

    def embed(self, texts):
        for text in texts:
            yield np.array(
                [-1.0, 0.0] if text == "neg" else [1.0, 0.0], dtype=np.float32
            )


@pytest.fixture
def fake(tmp_path, monkeypatch):
    embedder = FakeEmbedder()
    monkeypatch.setattr(index, "_embedder", lambda: embedder)
    monkeypatch.setenv("VREP_CACHE_DIR", str(tmp_path / "cache"))
    index._vectors_for.cache_clear()
    yield embedder
    index._vectors_for.cache_clear()


def test_search_returns_sorted_limited_results_with_srch01_fields(fake):
    results = index.search("joint target position", max_results=5)

    assert len(results) == 5
    assert [r["score"] for r in results] == sorted(
        (r["score"] for r in results), reverse=True
    )
    assert all(
        set(r) == {"name", "kind", "namespace", "description", "score"} for r in results
    )
    assert all(len(r["description"]) <= 200 for r in results)
    assert all(0 <= r["score"] <= 100 for r in results)


def test_search_aligns_cache_rows_with_entry_names(fake):
    entry = catalog.get("sim.setJointTargetPosition")

    results = index.search(
        f"sim.set Joint Target Position: {entry['description']}", max_results=1
    )

    assert results[0]["name"] == "sim.setJointTargetPosition"
    assert results[0]["score"] == 100.0


def test_search_truncates_descriptions_longer_than_200_chars(fake):
    entry = catalog.get("sim.setJointTargetPosition")
    assert len(entry["description"]) > 200

    results = index.search(
        f"sim.set Joint Target Position: {entry['description']}", max_results=1
    )

    assert results[0]["description"] == entry["description"][:200]


def test_search_namespace_filter_returns_only_that_namespace(fake):
    results = index.search("create dialog", max_results=50, namespace="simUI")

    assert results
    assert {r["namespace"] for r in results} == {"simUI"}


@pytest.mark.parametrize("kind", ["function", "constant"])
def test_search_kind_filter_returns_only_that_kind(fake, kind):
    results = index.search("handle", max_results=50, kind=kind)

    assert results
    assert {r["kind"] for r in results} == {kind}


def test_first_search_embeds_all_entries_and_writes_cache_file(fake, tmp_path):
    index.search("handle")

    paths = list((tmp_path / "cache").glob("index-????????????????.npy"))
    assert len(paths) == 1
    assert np.load(paths[0]).shape == (975, DIM)
    assert len(fake.calls[0]) == 975
    assert ": " in fake.calls[0][0]


def test_indexed_text_splits_camel_case_names_before_the_description(fake):
    index.search("handle")

    entry = catalog.get("sim.setJointTargetPosition")
    assert f"sim.set Joint Target Position: {entry['description']}" in fake.calls[0]


def test_cache_written_before_text_format_change_is_not_reused(fake, tmp_path):
    cache = tmp_path / "cache"
    cache.mkdir()
    old_name = f"index-{catalog.catalog_hash()[:16]}.npy"
    np.save(cache / old_name, np.zeros((975, DIM), dtype=np.float32))

    index.search("handle")

    assert len(fake.calls[0]) == 975


def test_second_search_with_fresh_state_loads_cache_and_embeds_only_query(fake):
    index.search("handle")
    index._vectors_for.cache_clear()
    fake.calls.clear()

    index.search("joint")

    assert fake.calls == [["joint"]]


def test_changed_catalog_writes_a_new_cache_file(fake, data_dir, tmp_path):
    index.search("handle")
    (data_dir / "simVision.json").write_text("[]")
    catalog._load.cache_clear()
    fake.calls.clear()

    index.search("handle")

    assert len(list((tmp_path / "cache").glob("index-*.npy"))) == 2
    assert len(fake.calls[0]) == 975 - 46


@pytest.mark.parametrize(
    "kwargs, message",
    [
        ({"query": ""}, "query must not be empty"),
        ({"query": "   "}, "query must not be empty"),
        ({"query": "x", "max_results": 0}, "max_results must be between 1 and 50"),
        ({"query": "x", "max_results": 51}, "max_results must be between 1 and 50"),
        (
            {"query": "x", "namespace": "foo"},
            "Unknown namespace 'foo'. Valid: sim, simUI, simROS2, simVision",
        ),
        ({"query": "x", "kind": "method"}, "kind must be 'function' or 'constant'"),
    ],
)
def test_search_invalid_input_raises_exact_message_before_embedding(
    fake, kwargs, message
):
    with pytest.raises(catalog.VrepError) as exc:
        index.search(**kwargs)

    assert str(exc.value) == message
    assert fake.calls == []


def test_search_accepts_max_results_bounds(fake):
    assert len(index.search("handle", max_results=1)) == 1
    assert len(index.search("handle", max_results=50)) == 50


def test_search_score_is_cosine_times_100_clamped_to_0_100(tmp_path, monkeypatch):
    monkeypatch.setattr(index, "_embedder", lambda: AxisEmbedder())
    monkeypatch.setenv("VREP_CACHE_DIR", str(tmp_path))
    index._vectors_for.cache_clear()

    same = index.search("pos", max_results=3)
    opposite = index.search("neg", max_results=3)
    index._vectors_for.cache_clear()

    assert [r["score"] for r in same] == [100.0] * 3
    assert [r["score"] for r in opposite] == [0.0] * 3


def test_search_wraps_model_failure_as_index_unavailable(tmp_path, monkeypatch):
    def broken():
        raise RuntimeError("boom")

    monkeypatch.setattr(index, "_embedder", broken)
    monkeypatch.setenv("VREP_CACHE_DIR", str(tmp_path))
    index._vectors_for.cache_clear()

    with pytest.raises(catalog.VrepError) as exc:
        index.search("handle")

    assert str(exc.value) == "Search index unavailable: boom"


def test_search_keeps_catalog_error_message_when_catalog_missing(fake, data_dir):
    (data_dir / "simUI.json").unlink()
    catalog._load.cache_clear()

    with pytest.raises(catalog.VrepError, match=r"^Catalog file .*simUI.json missing"):
        index.search("handle")


def test_importing_index_does_not_instantiate_the_embedder(monkeypatch):
    import fastembed

    created = []
    monkeypatch.setattr(
        fastembed, "TextEmbedding", lambda *a, **k: created.append(a) or object()
    )

    importlib.reload(index)

    assert created == []
