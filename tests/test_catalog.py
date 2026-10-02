import json
import shutil

import pytest

from vrep_mcp import catalog


@pytest.fixture
def data_dir(tmp_path, monkeypatch):
    for f in catalog._FILES:
        shutil.copy(catalog._data_dir() / f, tmp_path / f)
    monkeypatch.setenv("VREP_DATA_DIR", str(tmp_path))
    return tmp_path


def test_list_namespaces_returns_cat01_counts_in_order():
    assert catalog.list_namespaces() == [
        {"namespace": "sim", "functions": 323, "constants": 399},
        {"namespace": "simUI", "functions": 146, "constants": 0},
        {"namespace": "simROS2", "functions": 61, "constants": 0},
        {"namespace": "simVision", "functions": 46, "constants": 0},
    ]


def test_get_serial_read_uses_lua_fallback_when_python_raw_missing():
    e = catalog.get("sim.serialRead")
    assert [p["param_name"] for p in e["params"]] == [
        "portHandle",
        "dataLengthToRead",
        "blockingOperation",
        "closingString",
        "timeout",
    ]
    assert e["signature"].startswith("string data = sim.serialRead(")


def test_get_unknown_name_raises_cat09_message():
    with pytest.raises(catalog.VrepError) as exc:
        catalog.get("sim.nope")
    assert str(exc.value) == "Unknown function 'sim.nope'. Use search_functions."


def test_entries_missing_file_raises_ops04_message(data_dir):
    (data_dir / "simUI.json").unlink()
    with pytest.raises(
        catalog.VrepError,
        match=rf"^Catalog file {data_dir}/simUI.json missing or invalid: ",
    ):
        catalog.entries()


def test_entries_corrupt_json_raises_ops04_message(data_dir):
    (data_dir / "constants.json").write_text("{not json")
    with pytest.raises(
        catalog.VrepError,
        match=rf"^Catalog file {data_dir}/constants.json missing or invalid: ",
    ):
        catalog.entries()


def test_catalog_hash_changes_when_one_file_changes(data_dir):
    before = catalog.catalog_hash()
    (data_dir / "simVision.json").write_text(json.dumps([]))
    assert catalog.catalog_hash() != before


def test_catalog_hash_is_stable_for_identical_bytes(data_dir):
    assert catalog.catalog_hash() == catalog.catalog_hash()
