import asyncio
import json
import os
import subprocess
import threading
from pathlib import Path

from fastmcp import Client
from fastmcp.client.transports import StdioTransport

ROOT = Path(__file__).parents[1]
TOOLS = {"list_namespaces", "search_functions", "get_function_schema", "call_function"}
INHERITED_ENV = ("PATH", "HOME")


def spawn_client(extra_env=None):
    # why: StdioTransport passes only an allowlist of env vars, so uv needs PATH/HOME explicitly
    env = {k: os.environ[k] for k in INHERITED_ENV if k in os.environ}
    env.update(extra_env or {})
    transport = StdioTransport(
        "uv", ["run", "--project", str(ROOT), "vrep-mcp"], env=env, cwd=str(ROOT)
    )
    return Client(transport)


def test_stdio_session_lists_four_tools_and_returns_get_object_schema():
    async def go():
        async with spawn_client() as client:
            tools = await client.list_tools()
            schema = await client.call_tool(
                "get_function_schema", {"name": "sim.getObject"}
            )
            return tools, schema

    tools, schema = asyncio.run(go())

    assert {t.name for t in tools} == TOOLS
    assert schema.data["name"] == "sim.getObject"
    assert schema.data["inputSchema"]["required"] == ["objectPath"]


def test_stdout_carries_only_json_rpc_with_verbose_2_and_a_real_zmq_call():
    # hazard: the ZMQ client prints to stdout when VERBOSE > 0; reaching it proves verbose=0
    requests = [
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "t", "version": "0"},
            },
        },
        {"jsonrpc": "2.0", "method": "notifications/initialized"},
        {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/call",
            "params": {
                "name": "call_function",
                "arguments": {
                    "name": "sim.getObject",
                    "arguments": {"objectPath": "/Floor"},
                },
            },
        },
    ]
    env = {**os.environ, "VERBOSE": "2", "VREP_PORT": "1", "VREP_TIMEOUT": "1"}

    proc = subprocess.Popen(
        ["uv", "run", "--project", str(ROOT), "vrep-mcp"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        env=env,
        cwd=ROOT,
    )
    watchdog = threading.Timer(60, proc.kill)
    watchdog.start()
    messages = []
    try:
        proc.stdin.write("".join(json.dumps(r) + "\n" for r in requests))
        proc.stdin.flush()
        # invariant: stdin stays open until the reply arrives; EOF would stop the server first
        for line in proc.stdout:
            if line.strip():
                messages.append(json.loads(line))
            if messages and messages[-1].get("id") == 2:
                break
    finally:
        watchdog.cancel()
        proc.kill()

    assert all(m["jsonrpc"] == "2.0" for m in messages)
    reply = messages[-1]
    assert reply["result"]["isError"] is True
    assert "CoppeliaSim not reachable at localhost:1 (timeout 1s)." in json.dumps(reply)
