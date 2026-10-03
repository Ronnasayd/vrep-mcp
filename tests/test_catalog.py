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


def _input_schema(name):
    return catalog.schema(name)["inputSchema"]


def test_schema_function_has_cat02_shape_and_parameter_order():
    s = catalog.schema("sim.setJointTargetPosition")
    assert {
        "name",
        "kind",
        "namespace",
        "signature",
        "description",
        "url",
        "returns",
        "inputSchema",
    } <= set(s)
    assert (s["kind"], s["namespace"]) == ("function", "sim")
    assert list(s["inputSchema"]["properties"]) == [
        "objectHandle",
        "targetPosition",
        "motionParams",
    ]


def test_schema_required_excludes_defaulted_params_and_maps_types():
    s = _input_schema("sim.setJointTargetPosition")
    assert s["required"] == ["objectHandle", "targetPosition"]
    assert s["properties"]["targetPosition"] == {
        "x-vrep-type": "float",
        "type": "number",
    }
    assert s["properties"]["motionParams"]["type"] == "array"


def test_schema_unmapped_doc_type_has_no_type_key_but_keeps_x_vrep_type():
    prop = _input_schema("sim.serialSend")["properties"]["data"]
    assert "type" not in prop
    assert prop["x-vrep-type"] == "buffer"


def test_schema_misaligned_param_docs_omit_property_descriptions():
    props = _input_schema("sim.setJointTargetPosition")["properties"]
    assert all("description" not in p for p in props.values())


def test_schema_aligned_param_docs_set_property_descriptions():
    props = _input_schema("sim.setExplicitHandling")["properties"]
    assert props["objectHandle"]["description"] == "handle of a scene object."


def test_schema_lua_fallback_required_excludes_defaulted_params():
    required = _input_schema("sim.serialRead")["required"]
    assert required == ["portHandle", "dataLengthToRead", "blockingOperation"]


def test_schema_constant_returns_cat08_shape():
    assert catalog.schema("sim.handle_world") == {
        "name": "sim.handle_world",
        "kind": "constant",
        "namespace": "sim",
        "type": "int",
    }
