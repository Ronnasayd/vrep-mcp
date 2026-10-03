import json

import pytest

from vrep_mcp import catalog


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


@pytest.mark.parametrize("filename", catalog._FILES)
def test_catalog_hash_changes_when_any_one_file_changes(data_dir, filename):
    before = catalog.catalog_hash()
    (data_dir / filename).write_text(json.dumps([]))
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


def test_to_positional_maps_named_arguments_in_schema_order():
    assert catalog.to_positional(
        "sim.setJointTargetPosition", {"targetPosition": 1.5, "objectHandle": 5}
    ) == [5, 1.5]


def test_to_positional_no_param_function_with_empty_arguments_returns_empty_list():
    assert catalog.to_positional("sim.getSimulationState", {}) == []


def test_to_positional_stops_after_last_given_optional():
    args = {"objectHandle": 5, "targetPosition": 1.5, "motionParams": [1.0]}
    assert catalog.to_positional("sim.setJointTargetPosition", args) == [5, 1.5, [1.0]]


@pytest.mark.parametrize(
    "name, arguments, message",
    [
        (
            "sim.setJointTargetPosition",
            {"objectHandle": 1},
            "Missing required argument(s): ['targetPosition']",
        ),
        (
            "sim.setJointTargetPosition",
            {"objectHandle": 1, "targetPosition": 0, "x": 1},
            "Unknown argument(s) ['x']; expected ['objectHandle', 'targetPosition', 'motionParams']",
        ),
        (
            "sim.getObjectPosition",
            {"relativeToObjectHandle": 1, "objectHandle": 2, "extra": 3},
            "Unknown argument(s) ['extra']; expected ['objectHandle', 'relativeToObjectHandle']",
        ),
        (
            "sim.packTable",
            {"packingScheme": 1},
            "Missing required argument(s): ['aTable']",
        ),
        (
            "sim.setJointTargetPosition",
            {"objectHandle": "a", "targetPosition": 0},
            "Argument 'objectHandle' expected integer, got string",
        ),
    ],
)
def test_to_positional_raises_exact_spec_messages(name, arguments, message):
    with pytest.raises(catalog.VrepError) as exc:
        catalog.to_positional(name, arguments)
    assert str(exc.value) == message


def test_to_positional_gap_before_later_argument_raises_cat06_message():
    with pytest.raises(catalog.VrepError) as exc:
        catalog.to_positional(
            "sim.serialRead",
            {
                "portHandle": 1,
                "dataLengthToRead": 2,
                "blockingOperation": True,
                "timeout": 1.0,
            },
        )
    assert (
        str(exc.value)
        == "Optional argument(s) ['closingString'] must be given because a later one is set"
    )


def test_to_positional_accepts_int_for_number():
    assert catalog.to_positional(
        "sim.setJointTargetPosition", {"objectHandle": 1, "targetPosition": 2}
    ) == [1, 2]


@pytest.mark.parametrize(
    "arguments, expected",
    [
        (
            {"objectHandle": True, "targetPosition": 1.0},
            "Argument 'objectHandle' expected integer, got boolean",
        ),
        (
            {"objectHandle": 1, "targetPosition": True},
            "Argument 'targetPosition' expected number, got boolean",
        ),
    ],
)
def test_to_positional_rejects_bool_for_integer_and_number(arguments, expected):
    with pytest.raises(catalog.VrepError) as exc:
        catalog.to_positional("sim.setJointTargetPosition", arguments)
    assert str(exc.value) == expected


@pytest.mark.parametrize("value", [b"x", 1, [1], {"a": 1}, None])
def test_to_positional_accepts_any_json_for_untyped_param(value):
    assert catalog.to_positional(
        "sim.serialSend", {"portHandle": 1, "data": value}
    ) == [1, value]


def test_to_positional_rejects_null_for_typed_param():
    with pytest.raises(catalog.VrepError) as exc:
        catalog.to_positional(
            "sim.setJointTargetPosition", {"objectHandle": None, "targetPosition": 1.0}
        )
    assert str(exc.value) == "Argument 'objectHandle' expected integer, got null"


def test_schema_signature_of_regular_function_is_its_python_raw():
    assert catalog.schema("sim.getObject")["signature"] == (
        "int objectHandle = sim.getObject(string objectPath, dict options = {})"
    )


@pytest.mark.parametrize(
    "name, param, vrep_type, json_type",
    [
        ("sim.setJointTargetPosition", "objectHandle", "int", "integer"),
        ("sim.getReferencedHandles", "tag", "string", "string"),
        ("sim.setStepping", "enable", "bool", "boolean"),
        ("sim.packTable", "aTable", "dict", "object"),
        ("sim.copyTable", "original", "map", "object"),
    ],
)
def test_schema_maps_doc_types_to_json_types_and_keeps_x_vrep_type(
    name, param, vrep_type, json_type
):
    prop = _input_schema(name)["properties"][param]

    assert prop["x-vrep-type"] == vrep_type
    assert prop["type"] == json_type


def test_schema_property_descriptions_are_stripped_of_surrounding_whitespace():
    props = _input_schema("sim.getScaledImage")["properties"]

    assert props["desiredResolutionOut"]["description"].endswith("bit-coded:")
    assert all(p["description"] == p["description"].strip() for p in props.values())


def test_to_positional_all_optional_function_with_empty_arguments_returns_empty_list():
    assert catalog.to_positional("sim.stopSimulation", {}) == []


def test_schema_returns_and_url_come_from_the_catalog_entry():
    s = catalog.schema("sim.getObject")

    assert s["returns"] == [{"return_type": "int", "return_name": "objectHandle"}]
    assert s["url"] == "https://manual.coppeliarobotics.com/en/sim/simGetObject.htm"


def test_schema_param_named_id_is_required_despite_defaulted_id_suffixed_params():
    s = _input_schema("simUI.addTreeItem")

    assert s["required"] == ["handle", "id", "item_id", "text"]


def test_return_variable_does_not_make_param_optional():
    # sim.moduleEntry: `int handle = sim.moduleEntry(int handle, ...)` — handle is required (CAT-02, CALL-04)
    assert "handle" in catalog.schema("sim.moduleEntry")["inputSchema"]["required"]
    with pytest.raises(catalog.VrepError, match="Missing required argument"):
        catalog.to_positional("sim.moduleEntry", {})
