"""FastMCP server: 4 tools that cover the entire CoppeliaSim API."""

from __future__ import annotations

import functools
import logging
import sys
from collections.abc import Callable
from typing import Any

from fastmcp import FastMCP
from fastmcp.exceptions import ToolError

from . import bridge, catalog, index

mcp = FastMCP(
    "vrep-mcp",
    instructions=(
        "CoppeliaSim API proxy. Flow: search_functions -> get_function_schema (always, "
        "args must match inputSchema) -> call_function. Names are "
        "'<namespace>.<method>', e.g. 'sim.getObject'. Constants (e.g. "
        "'sim.handle_world') are readable via call_function with no arguments."
    ),
)


def _as_tool_error(fn: Callable[..., Any]) -> Callable[..., Any]:
    """Keep domain modules free of FastMCP: map VrepError to ToolError here."""

    @functools.wraps(fn)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return fn(*args, **kwargs)
        except catalog.VrepError as exc:
            raise ToolError(str(exc)) from exc

    return wrapper


@mcp.tool
@_as_tool_error
def list_namespaces() -> list[dict[str, Any]]:
    """List API namespaces (sim, simUI, simROS2, simVision) with function/constant counts."""
    return catalog.list_namespaces()


@mcp.tool
@_as_tool_error
def search_functions(
    query: str,
    max_results: int = 10,
    namespace: str | None = None,
    kind: str | None = None,
) -> list[dict[str, Any]]:
    """Semantic search (English or Portuguese) over function/constant names and descriptions.

    `namespace`: sim | simUI | simROS2 | simVision. `kind`: function | constant.
    """
    return index.search(query, max_results, namespace, kind)


@mcp.tool
@_as_tool_error
def get_function_schema(name: str) -> dict[str, Any]:
    """Signature, docs, return types and JSON inputSchema for e.g. 'sim.setJointTargetPosition'."""
    return catalog.schema(name)


@mcp.tool
@_as_tool_error
def call_function(name: str, arguments: dict[str, Any] | None = None) -> Any:
    """Execute an API function (or read a constant) on the running CoppeliaSim via ZMQ remote API.

    `arguments` maps parameter names to values. Env: VREP_HOST (localhost),
    VREP_PORT (23000), VREP_TIMEOUT (30 seconds).
    """
    return bridge.call(name, arguments)


def main() -> None:
    # invariant: stdout carries JSON-RPC only (OPS-02); every log goes to stderr
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    mcp.run()


if __name__ == "__main__":
    main()
