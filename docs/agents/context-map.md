## Context Map

### Task Interpretation

- Restated task: build `vrep-mcp`, an MCP server that exposes the whole CoppeliaSim API (576 functions in `sim`/`simUI`/`simROS2`/`simVision` plus 399 `sim` constants) through only 4 tools, mirroring mcp-manager's discover → schema → call flow.
- Task type: feature
- Assumptions: `processed/*.json` is the canonical catalog (`simDocs/` stubs are generated from the same data and drop default-value info); transport is the ZMQ remote API (`coppeliasim-zmqremoteapi-client`, default port 23000); draft code under `src/vrep_mcp/` is disposable and must be re-validated against the spec.
- Anchors: `catalog.entries` (src/vrep_mcp/catalog.py) — confirmed by: Read, pytest; `processed/sim.json` data shape — confirmed by: python inspection, grep

### Files to Modify

| File                    | Purpose                                                     | Changes Needed                                                                                                                |
| ----------------------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| src/vrep_mcp/catalog.py | catalog load, search, schema, arg mapping, ZMQ call (draft) | handle `python_raw=None` (14 sim funcs), misaligned `params_definitions` (123 sim funcs), error/timeout policy, safety policy |
| src/vrep_mcp/server.py  | FastMCP server exposing the 4 tools (draft)                 | finalize tool names/descriptions, error mapping to MCP errors                                                                 |
| tests/test_catalog.py   | offline unit tests with fake API (draft)                    | add cases for data anomalies, serialization, e2e via `fastmcp.Client`                                                         |
| pyproject.toml          | uv project, deps, entrypoint (draft)                        | confirm fastmcp major (mcp-manager pins `<3`, PyPI latest 4.0.10)                                                             |
| processed/sim.json      | source catalog (input data)                                 | none expected; anomalies handled in code                                                                                      |

### Dependencies (may need updates)

| File                     | Relationship                                                                   |
| ------------------------ | ------------------------------------------------------------------------------ |
| processed/constants.json | constants list, no prefix, all typed `int`                                     |
| processed/simUI.json     | simUI catalog, same schema as sim minus params_definitions/returns_definitions |
| processed/simROS2.json   | simROS2 catalog, same schema as simUI                                          |
| processed/simVision.json | simVision catalog, same schema as simUI                                        |
| simDocs/sim.py           | generated Python stubs, same 576 functions, lose default-value info            |
| uv.lock                  | lockfile produced by draft `uv sync`                                           |

### Test Files

| Test                  | Coverage                                                                                                   |
| --------------------- | ---------------------------------------------------------------------------------------------------------- |
| tests/test_catalog.py | 5 offline tests: namespaces, search, schema required/optional, positional mapping + constants, error cases |

### Reference Patterns

| File                                     | Pattern                                                               |
| ---------------------------------------- | --------------------------------------------------------------------- |
| ../mcp-manager/src/tools/call_tool.py    | argument validation against inputSchema before dispatch               |
| ../mcp-manager/src/tools/search_tools.py | cached catalog load + ranked search results (`server`,`name`,`score`) |
| ../mcp-manager/pyproject.toml            | fastmcp `>=2,<3`, hatchling, script entrypoints                       |

### Prior Decisions / Gotchas

- No prior ai-memory pages for vrep-mcp.
- Global memory: mcp-manager `sequentialthinking` reported broken on 2026-09-11; worked in this session.
- `.mcp.json` and sibling repos are symlinks/paths outside the project; protect_files hook denies reading them.

### Risk Assessment

- [ ] Breaking changes to public API
- [ ] Database migrations needed
- [x] Configuration changes required — register server in `.mcp.json` / mcp-manager `backends.json`; env `VREP_HOST`/`VREP_PORT`
- [x] No test coverage for anchor(s) — no e2e against real CoppeliaSim (not installed locally)
- [x] Data quality — 14 sim functions without `python_raw`, 123 with `params_definitions` length mismatch; doc-derived types (`list`/`dict`/`func`/`buffer`) may differ from runtime
- [x] Safety — `call_function` can run destructive calls (`sim.quitSimulator`, `sim.removeObjects`, `sim.saveScene`, script execution)

### Not Checked

- ZMQ client timeout/reconnect behavior (context7 has no client docs; needs real simulator).
- mcp-manager `backends.json` format (outside project, hook-protected).
- Behavior of `func`-typed params (callbacks) over remote API.
