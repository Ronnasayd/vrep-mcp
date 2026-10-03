import importlib
import threading
import time

import coppeliasim_zmqremoteapi_client as zmq_client
import pytest
import zmq

from vrep_mcp import bridge, catalog


class FakeSocket:
    def __init__(self):
        self.options = {}
        self.closed = False

    def setsockopt(self, option, value):
        self.options[option] = value

    def close(self):
        self.closed = True


class FakeContext:
    def __init__(self):
        self.terminated = False

    def term(self):
        self.terminated = True


class FakeNamespace:
    def __init__(self, client):
        self.client = client
        self.handle_world = -6

    def getObject(self, path):
        return self.client.run("getObject", path)

    def getSimulationState(self):
        return self.client.run("getSimulationState")

    def serialSend(self, port, data):
        return self.client.run("serialSend", port, data)

    def setJointTargetPosition(self, handle, position, params=None):
        return self.client.run("setJointTargetPosition", handle, position)

    def inputDialog(self):
        return self.client.run("inputDialog")

    def slow(self):
        return self.client.run("slow")


class FakeClient:
    instances = []
    results = {}
    errors = {}

    def __init__(self, host, port, verbose=None):
        self.args = (host, port, verbose)
        self.socket = FakeSocket()
        self.context = FakeContext()
        self.calls = []
        FakeClient.instances.append(self)

    def require(self, name):
        self.required = name
        return FakeNamespace(self)

    def run(self, method, *args):
        self.calls.append((method, args))
        if method in FakeClient.errors:
            raise FakeClient.errors[method]
        return FakeClient.results.get(method)


@pytest.fixture
def fake_api(monkeypatch):
    FakeClient.instances, FakeClient.results, FakeClient.errors = [], {}, {}
    monkeypatch.setattr(zmq_client, "RemoteAPIClient", FakeClient)
    for var in ("VREP_HOST", "VREP_PORT", "VREP_TIMEOUT"):
        monkeypatch.delenv(var, raising=False)
    bridge._client = None
    yield FakeClient
    bridge._client = None


def test_call_invokes_function_positionally_and_builds_client_lazily(fake_api):
    fake_api.results["setJointTargetPosition"] = None
    assert fake_api.instances == []

    bridge.call(
        "sim.setJointTargetPosition", {"targetPosition": 1.5, "objectHandle": 5}
    )

    client = fake_api.instances[0]
    assert client.required == "sim"
    assert client.calls == [("setJointTargetPosition", (5, 1.5))]


def test_call_builds_client_with_env_host_port_verbose_zero_and_timeouts(
    fake_api, monkeypatch
):
    monkeypatch.setenv("VREP_HOST", "10.0.0.7")
    monkeypatch.setenv("VREP_PORT", "24000")
    monkeypatch.setenv("VREP_TIMEOUT", "2.5")

    bridge.call("sim.getSimulationState")

    client = fake_api.instances[0]
    assert client.args == ("10.0.0.7", 24000, 0)
    assert client.socket.options[zmq.RCVTIMEO] == 2500
    assert client.socket.options[zmq.SNDTIMEO] == 2500
    assert client.socket.options[zmq.LINGER] == 0


def test_call_requires_the_namespace_of_the_called_entry(fake_api):
    bridge.call("simUI.inputDialog")

    assert fake_api.instances[0].required == "simUI"


def test_call_reuses_one_client_across_calls(fake_api):
    bridge.call("sim.getSimulationState")
    bridge.call("sim.getSimulationState")

    assert len(fake_api.instances) == 1


def test_importing_bridge_does_not_create_a_client(fake_api):
    importlib.reload(bridge)

    assert fake_api.instances == []


def test_call_converts_tuple_to_list_and_none_to_null(fake_api):
    fake_api.results["getObject"] = (1, 2, [3])
    fake_api.results["getSimulationState"] = None

    assert bridge.call("sim.getObject", {"objectPath": "/Floor"}) == [1, 2, [3]]
    assert bridge.call("sim.getSimulationState") is None


@pytest.mark.parametrize(
    "value, expected",
    [(b"hi", "aGk="), (bytearray(b"hi"), "aGk=")],
)
def test_call_converts_bytes_to_base64(fake_api, value, expected):
    fake_api.results["getObject"] = value

    assert bridge.call("sim.getObject", {"objectPath": "/x"}) == expected


def test_jsonable_converts_nested_values_and_falls_back_to_repr():
    marker = object()

    assert bridge.jsonable({"a": (1, b"hi"), "b": None, "c": marker}) == {
        "a": [1, "aGk="],
        "b": None,
        "c": repr(marker),
    }


def test_call_constant_returns_value_and_ignores_arguments(fake_api):
    result = bridge.call("sim.handle_world", {"bogus": 1})

    assert result == -6
    assert fake_api.instances[0].calls == []


def test_call_timeout_raises_call09_message_and_discards_client(fake_api, monkeypatch):
    monkeypatch.setenv("VREP_HOST", "h")
    monkeypatch.setenv("VREP_PORT", "1234")
    monkeypatch.setenv("VREP_TIMEOUT", "5")
    fake_api.errors["getSimulationState"] = zmq.Again()

    with pytest.raises(catalog.VrepError) as exc:
        bridge.call("sim.getSimulationState")

    assert str(exc.value) == (
        "CoppeliaSim not reachable at h:1234 (timeout 5s). "
        "Start CoppeliaSim with the ZMQ remote API add-on and retry."
    )
    dead = fake_api.instances[0]
    assert (dead.socket.closed, dead.context.terminated) == (True, True)


def test_call_after_timeout_opens_a_new_connection(fake_api):
    fake_api.errors["getSimulationState"] = zmq.Again()
    with pytest.raises(catalog.VrepError):
        bridge.call("sim.getSimulationState")
    fake_api.errors.clear()
    fake_api.results["getSimulationState"] = 0

    result = bridge.call("sim.getSimulationState")

    assert result == 0
    assert len(fake_api.instances) == 2
    assert fake_api.instances[1].calls == [("getSimulationState", ())]


def test_call_simulator_error_raises_call11_message_and_keeps_connection(fake_api):
    fake_api.errors["getObject"] = Exception("boom")

    with pytest.raises(catalog.VrepError) as exc:
        bridge.call("sim.getObject", {"objectPath": "/x"})
    bridge.call("sim.getSimulationState")

    assert str(exc.value) == "CoppeliaSim error in sim.getObject: boom"
    assert len(fake_api.instances) == 1


def test_call_function_missing_in_connected_version_raises_not_available(fake_api):
    with pytest.raises(catalog.VrepError) as exc:
        bridge.call("sim.getObjectPosition", {"objectHandle": 1})

    assert str(exc.value) == (
        "CoppeliaSim error in sim.getObjectPosition: "
        "function not available in the connected CoppeliaSim"
    )


def test_call_invalid_arguments_raise_before_creating_a_client(fake_api):
    with pytest.raises(catalog.VrepError) as exc:
        bridge.call("sim.setJointTargetPosition", {"objectHandle": 1})

    assert str(exc.value) == "Missing required argument(s): ['targetPosition']"
    assert fake_api.instances == []


def test_call_unknown_name_raises_before_creating_a_client(fake_api):
    with pytest.raises(catalog.VrepError) as exc:
        bridge.call("sim.nope")

    assert str(exc.value) == "Unknown function 'sim.nope'. Use search_functions."
    assert fake_api.instances == []


def test_concurrent_calls_never_overlap_inside_the_api(fake_api):
    state = {"active": 0, "max": 0}

    def slow_run(method, *args):
        state["active"] += 1
        state["max"] = max(state["max"], state["active"])
        time.sleep(0.05)
        state["active"] -= 1

    bridge.call("sim.getSimulationState")
    fake_api.instances[0].run = slow_run
    threads = [
        threading.Thread(target=bridge.call, args=("sim.getSimulationState",))
        for _ in range(4)
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert state["max"] == 1
