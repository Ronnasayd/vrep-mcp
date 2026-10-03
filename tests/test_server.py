import asyncio
import json
import re
import zlib

import numpy as np
import pytest
import zmq
from fastmcp import Client
from fastmcp.exceptions import ToolError

from vrep_mcp import bridge, index

DIM = 8192
TOOLS = {"list_namespaces", "search_functions", "get_function_schema", "call_function"}


class FakeEmbedder:
    def embed(self, texts):
        for text in texts:
            vec = np.zeros(DIM, dtype=np.float32)
            for word in re.findall(r"[a-z0-9]+", text.lower()):
                vec[zlib.crc32(word.encode()) % DIM] += 1.0
            yield vec


class FakeSocket:
    def setsockopt(self, *_):
        pass

    def close(self):
        pass


class FakeContext:
    def term(self):
        pass


class FakeNamespace:
    def __init__(self, behaviour):
        self.behaviour = behaviour

    def getObject(self, path):
        return self.behaviour(path)


class FakeClient:
    socket = FakeSocket()
    context = FakeContext()
    behaviour = staticmethod(lambda path: 42)

    def require(self, _name):
        return FakeNamespace(FakeClient.behaviour)


@pytest.fixture
def wired(tmp_path, monkeypatch):
    from vrep_mcp import server

    monkeypatch.setattr(index, "_embedder", lambda: FakeEmbedder())
    monkeypatch.setenv("VREP_CACHE_DIR", str(tmp_path))
    monkeypatch.setattr(bridge, "_new_client", lambda: FakeClient())
    FakeClient.behaviour = staticmethod(lambda path: 42)
    index._vectors_for.cache_clear()
    bridge._client = None
    yield server.mcp
    index._vectors_for.cache_clear()
    bridge._client = None


def run(mcp, coro_fn):
    async def go():
        async with Client(mcp) as client:
            return await coro_fn(client)

    return asyncio.run(go())


def call(mcp, tool, arguments):
    """Wire payload: the JSON text the client receives."""
    result = run(mcp, lambda c: c.call_tool(tool, arguments))
    return json.loads(result.content[0].text)


def error_of(mcp, tool, arguments):
    with pytest.raises(ToolError) as exc:
        call(mcp, tool, arguments)
    return str(exc.value)


def test_server_lists_exactly_the_four_tools(wired):
    tools = run(wired, lambda c: c.list_tools())

    assert {t.name for t in tools} == TOOLS


def test_list_namespaces_returns_cat01_counts(wired):
    result = call(wired, "list_namespaces", {})

    assert result[0] == {"namespace": "sim", "functions": 323, "constants": 399}
    assert [d["namespace"] for d in result] == [
        "sim",
        "simUI",
        "simROS2",
        "simVision",
    ]


def test_search_functions_returns_srch01_items_filtered_by_kind(wired):
    result = call(
        wired,
        "search_functions",
        {"query": "handle world", "max_results": 3, "kind": "constant"},
    )

    assert len(result) == 3
    assert {r["kind"] for r in result} == {"constant"}
    assert set(result[0]) == {"name", "kind", "namespace", "description", "score"}


def test_search_functions_returns_ten_results_by_default(wired):
    assert len(call(wired, "search_functions", {"query": "handle"})) == 10


def test_search_functions_empty_query_returns_srch08_error(wired):
    assert error_of(wired, "search_functions", {"query": " "}) == (
        "query must not be empty"
    )


def test_get_function_schema_returns_cat02_schema(wired):
    result = call(wired, "get_function_schema", {"name": "sim.getObject"})

    assert result["name"] == "sim.getObject"
    assert result["inputSchema"]["required"] == ["objectPath"]


def test_get_function_schema_unknown_name_returns_cat09_error(wired):
    assert error_of(wired, "get_function_schema", {"name": "sim.nope"}) == (
        "Unknown function 'sim.nope'. Use search_functions."
    )


def test_call_function_returns_simulator_value(wired):
    result = call(
        wired,
        "call_function",
        {"name": "sim.getObject", "arguments": {"objectPath": "/Floor"}},
    )

    assert result == 42


def test_call_function_missing_argument_returns_call04_error(wired):
    assert error_of(wired, "call_function", {"name": "sim.getObject"}) == (
        "Missing required argument(s): ['objectPath']"
    )


def test_call_function_timeout_returns_call09_error(wired):
    def timeout(_path):
        raise zmq.Again()

    FakeClient.behaviour = staticmethod(timeout)

    message = error_of(
        wired,
        "call_function",
        {"name": "sim.getObject", "arguments": {"objectPath": "/x"}},
    )

    assert message.startswith(
        "CoppeliaSim not reachable at localhost:23000 (timeout 30s)."
    )
