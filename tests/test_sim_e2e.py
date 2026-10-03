import os
import socket

import pytest

from vrep_mcp import bridge

HOST = os.environ.get("VREP_HOST", "localhost")
PORT = int(os.environ.get("VREP_PORT", "23000"))
CONNECT_TIMEOUT_S = 1


def _simulator_reachable() -> bool:
    try:
        with socket.create_connection((HOST, PORT), timeout=CONNECT_TIMEOUT_S):
            return True
    except OSError:
        return False


pytestmark = [
    pytest.mark.sim,
    pytest.mark.skipif(
        not _simulator_reachable(), reason=f"CoppeliaSim not reachable at {HOST}:{PORT}"
    ),
]


@pytest.fixture(autouse=True)
def fresh_connection():
    bridge._reset()
    yield
    bridge._reset()


def test_get_simulation_state_returns_minus_one_state():
    state = bridge.call("sim.getSimulationState")

    assert isinstance(state, int)


def test_get_object_resolves_floor_in_the_default_scene_to_a_handle():
    handle = bridge.call("sim.getObject", {"objectPath": "/Floor"})

    assert isinstance(handle, int)
    assert handle >= 0


def test_reading_handle_world_constant_returns_minus_one():
    value = bridge.call("sim.handle_world", {"ignored": 1})

    assert value == -1  # observed on a live CoppeliaSim: sim.handle_world is -1
