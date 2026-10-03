# ADR-001 – Expose the CoppeliaSim API through a 4-tool proxy

> **Date:** 2026-10-02
> **Status:** Accepted
> **Deciders:** Project owner (Ronnasayd)

## Context

The CoppeliaSim API has 576 functions across `sim`, `simUI`, `simROS2`, and `simVision`, plus 399 constants. MCP clients send every tool schema on every request. One tool per function would cost tens of thousands of tokens per request before the agent does any work. The owner already runs mcp-manager, which solves the same problem for MCP backends with a discover → schema → call flow.

## Decision

vrep-mcp is a standalone MCP server with exactly 4 tools: `list_namespaces`, `search_functions`, `get_function_schema`, `call_function`. The agent finds a function by semantic search, loads only that function's schema, and runs it by name. The catalog comes from the processed documentation in `processed/*.json`, not from introspecting a live simulator.

## Considered Alternatives

| Alternative                                            | Pros                                                                             | Cons                                                                                                          |
| ------------------------------------------------------ | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| One native MCP tool per function (~975 tools)          | Native client validation; no discovery step                                      | Tens of thousands of schema tokens per request; many clients cap tool counts                                  |
| Native tools registered as an mcp-manager backend      | Reuses mcp-manager's search/schema/call                                          | Couples two repos; the server is unusable without mcp-manager; the owner asked for a standalone 4-tool server |
| Build the catalog by introspecting a running simulator | Always matches the connected version                                             | No descriptions, types, or defaults; search and schema need a running simulator                               |
| **4-tool proxy over a doc-derived catalog (chosen)**   | Constant, small tool list; works offline for discovery; same flow as mcp-manager | Extra round-trips (search → schema → call); types come from docs and can drift from runtime                   |

## Consequences

- The `tools/list` payload stays under 2,000 tokens regardless of API size.
- Each call takes up to 3 round-trips. Agents must load the schema before calling.
- Validation is only as accurate as the documentation. Functions missing in older simulator versions fail at call time with an explicit "not available" error.
- Do not "simplify" this into one tool per function. That reintroduces the token cost this server exists to avoid.

## Related ADRs

- ADR-002 – No restriction on callable functions.
