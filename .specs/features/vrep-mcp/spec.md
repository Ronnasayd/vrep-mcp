# vrep-mcp Specification

## Problem Statement

The CoppeliaSim (V-REP) API has 576 functions across `sim`, `simUI`, `simROS2`, and `simVision`, plus 399 `sim` constants. Exposing each function as its own MCP tool would cost tens of thousands of schema tokens on every request. This feature works like mcp-manager: an MCP server exposes the whole API through 4 lightweight tools (discover → schema → call). The model loads only the schema it needs and runs the function against a running CoppeliaSim.

## Goals

- [ ] An agent can run any of the 576 catalog functions and read any of the 399 constants through only 4 MCP tools.
- [ ] `search_functions` returns the expected function among the top 5 results for natural-language queries in English or Portuguese (e.g. "set joint target position", "posição alvo da junta" → `sim.setJointTargetPosition`).
- [ ] A call against an unreachable CoppeliaSim returns an actionable error within `VREP_TIMEOUT` seconds and never hangs the server.

## Out of Scope

| Feature                                                   | Reason                                                                  |
| --------------------------------------------------------- | ----------------------------------------------------------------------- |
| Batch execution (multiple calls per `call_function`)      | User decision: one call per invocation, same as mcp-manager `call_tool` |
| Safety policy (denylist / read-only mode)                 | User decision: local personal use, full access                          |
| HTTP/SSE transport                                        | User decision: stdio only                                               |
| Registration in mcp-manager `backends.json` / `.mcp.json` | User decision: not requested; config files live outside this repo       |
| Callback (`func`) parameters                              | ZMQ remote API cannot carry client-side callables                       |
| Legacy remote API / WebSocket transports                  | ZMQ remote API is the current official client                           |
| Regenerating `processed/*.json` from the online docs      | Data is produced by the separate `python-docs-vrep` project             |
| Batch embedding of `simDocs/` stubs                       | Stubs come from the same data and drop default-value info               |

---

## Assumptions & Open Questions

| Assumption / decision                                                    | Chosen default                                                                                                                                                                                                       | Rationale                                                                                                            | Confirmed? |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---------- |
| Catalog source                                                           | `processed/*.json` (repo root; override via `VREP_DATA_DIR`)                                                                                                                                                         | Only source with default-value info (`python_raw`)                                                                   | y          |
| Constants namespace                                                      | All 399 entries in `constants.json` belong to `sim`                                                                                                                                                                  | File has no prefix; all names match `sim.*` constants                                                                | n          |
| Transport                                                                | `coppeliasim-zmqremoteapi-client` 2.x, `client.require(namespace)` (CoppeliaSim ≥ 4.6)                                                                                                                               | Official current client; `require` loads plugin namespaces                                                           | y          |
| Connection config                                                        | `VREP_HOST` (default `localhost`), `VREP_PORT` (default `23000`)                                                                                                                                                     | Client defaults                                                                                                      | y          |
| Call timeout                                                             | `VREP_TIMEOUT` seconds, default `30`                                                                                                                                                                                 | The client blocks forever on `recv`; long simulator calls (stepping, scene load) need room                           | y          |
| Safety                                                                   | No restriction; every catalog function is callable                                                                                                                                                                   | User decision                                                                                                        | y          |
| Search engine                                                            | fastembed, model `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`, cosine similarity, indexed text `"<name with camelCase split into words>: <description>"`, e.g. `sim.set Joint Target Position: ...` | User decision; multilingual queries. Amended: with the raw name SRCH-05 ranked 7th, with the split name it ranks 1st | y          |
| Index lifecycle                                                          | Built lazily on the first search, cached on disk at `VREP_CACHE_DIR` (default `~/.cache/vrep-mcp`), keyed by SHA-256 of the 5 catalog files                                                                          | User decision                                                                                                        | y          |
| Constants in search                                                      | Indexed; `kind` filter accepts `function` or `constant`                                                                                                                                                              | User decision                                                                                                        | y          |
| Entries without `python_raw` (14 `sim` functions, empty `python.params`) | Fall back to `lua` params and `lua_raw` for signature + optional detection                                                                                                                                           | Only data available; Lua and Python share parameter order                                                            | n          |
| `params_definitions` length ≠ params length (123 `sim` functions)        | Omit per-parameter descriptions for that function                                                                                                                                                                    | Misaligned zip would attach wrong docs                                                                               | n          |
| Type mapping                                                             | `int`→integer, `float`→number, `string`→string, `bool`→boolean, `list`/`float[]`/`int[]`→array, `dict`/`map`→object; any other type → no JSON `type` constraint                                                      | Doc types like `buffer`, `bytes`, `any`, custom structs have no safe JSON mapping                                    | n          |
| Optional parameter                                                       | A parameter is optional iff the signature contains `<name> =`                                                                                                                                                        | Only default-value signal in the data                                                                                | n          |
| fastmcp version                                                          | `>=2.0,<3`                                                                                                                                                                                                           | Same major as mcp-manager; known API                                                                                 | y          |
| Draft code                                                               | `src/vrep_mcp/` draft is the base for implementation                                                                                                                                                                 | User decision                                                                                                        | y          |

**Open questions:** none. Each is either resolved or logged above.

---

## User Stories

### P1: Read the catalog ⭐ MVP

**User Story**: As an LLM agent, I want to list namespaces and load one function's schema so that I can build correct arguments without loading the whole API.

**Why P1**: Without a schema, the agent cannot build valid calls.

**Acceptance Criteria**:

1. WHEN `list_namespaces` is called THEN the system SHALL return exactly 4 entries in order `sim`, `simUI`, `simROS2`, `simVision`, each with `namespace`, `functions`, `constants` counts equal to 323/399, 146/0, 61/0, 46/0. <!-- CAT-01 -->
2. WHEN `get_function_schema` is called with a function name such as `sim.setJointTargetPosition` THEN the system SHALL return `name`, `kind="function"`, `namespace`, `signature`, `description`, `url`, `returns`, and `inputSchema` (JSON Schema object with `properties` in catalog parameter order and `required`). <!-- CAT-02 -->
3. WHEN a schema is built THEN the system SHALL list in `required` exactly the parameters without a `<name> =` default in the signature (e.g. `sim.setJointTargetPosition` → `["objectHandle","targetPosition"]`). <!-- CAT-03 -->
4. WHEN a schema is built THEN the system SHALL map parameter types using the Type mapping assumption and SHALL keep the original doc type in `x-vrep-type`. <!-- CAT-04 -->
5. WHEN a function's `params_definitions` length equals its params length THEN the system SHALL set each property's `description` from the matching definition. <!-- CAT-05 -->
6. IF a function's `params_definitions` length differs from its params length THEN the system SHALL omit property descriptions for that function. <!-- CAT-06 -->
7. IF an entry has no `python_raw` THEN the system SHALL build the schema from its `lua` params and use `lua_raw` as `signature`. <!-- CAT-07 -->
8. WHEN `get_function_schema` is called with a constant name such as `sim.handle_world` THEN the system SHALL return `name`, `kind="constant"`, `namespace="sim"`, `type="int"`. <!-- CAT-08 -->
9. IF `get_function_schema` receives a name not in the catalog THEN the system SHALL return an MCP tool error with message `Unknown function '<name>'. Use search_functions.`. <!-- CAT-09 -->

**Independent Test**: Run the 2 tools through `fastmcp.Client` in-memory without CoppeliaSim and check the counts and the `sim.setJointTargetPosition` schema.

---

### P1: Search the catalog ⭐ MVP

**User Story**: As an LLM agent, I want to search functions by natural-language intent so that I find the right API name without knowing it.

**Why P1**: Discovery is the entry point of the flow.

**Acceptance Criteria**:

1. WHEN `search_functions(query)` is called THEN the system SHALL return at most `max_results` (default 10) items sorted by descending `score`, each with `name`, `kind`, `namespace`, `description` (≤ 200 chars), and `score` (cosine similarity × 100, range 0-100). <!-- SRCH-01 -->
2. WHEN `namespace` is given THEN the system SHALL return only items of that namespace. <!-- SRCH-02 -->
3. WHEN `kind` is given (`function` or `constant`) THEN the system SHALL return only items of that kind. <!-- SRCH-03 -->
4. WHEN the query is `set joint target position` THEN the system SHALL include `sim.setJointTargetPosition` among the top 5 results. <!-- SRCH-04 -->
5. WHEN the query is `posição alvo da junta` THEN the system SHALL include `sim.setJointTargetPosition` among the top 5 results. <!-- SRCH-05 -->
6. WHEN the first search runs and no cache file matches the catalog hash THEN the system SHALL embed all 975 entries and write the cache file `<VREP_CACHE_DIR>/index-<sha256[:16]>.npy` (sha256 of the catalog hash plus the indexed-text format version, so a format change invalidates old caches). <!-- SRCH-06 -->
7. WHEN a cache file matching the catalog hash exists THEN the system SHALL load it without re-embedding. <!-- SRCH-07 -->
8. IF `query` is empty or whitespace THEN the system SHALL return an MCP tool error `query must not be empty`. <!-- SRCH-08 -->
9. IF `max_results` is outside 1-50 THEN the system SHALL return an MCP tool error `max_results must be between 1 and 50`. <!-- SRCH-09 -->
10. IF `namespace` is not one of the 4 namespaces THEN the system SHALL return an MCP tool error `Unknown namespace '<ns>'. Valid: sim, simUI, simROS2, simVision`. <!-- SRCH-10 -->
11. IF `kind` is not `function` or `constant` THEN the system SHALL return an MCP tool error `kind must be 'function' or 'constant'`. <!-- SRCH-11 -->

**Independent Test**: Run searches through `fastmcp.Client` in-memory and check SRCH-04/05 rankings, filters, and that a second process start reuses the cache file (no embed call).

---

### P1: Execute a function ⭐ MVP

**User Story**: As an LLM agent, I want to run any catalog function with named arguments against a running CoppeliaSim so that I can control the simulation.

**Why P1**: This is the purpose of the server.

**Acceptance Criteria**:

1. WHEN `call_function(name, arguments)` is called with valid arguments THEN the system SHALL invoke `client.require(namespace).<method>(*positional)` where `positional` follows the schema parameter order and stops at the last provided argument. <!-- CALL-01 -->
2. WHEN the function returns THEN the system SHALL return the value converted to JSON, with tuples as arrays and `bytes`/`bytearray` as base64 strings. <!-- CALL-02 -->
3. WHEN `call_function` is called with a constant name THEN the system SHALL return the constant's value from `client.require("sim")` and ignore `arguments`. <!-- CALL-03 -->
4. IF a required argument is missing THEN the system SHALL return an MCP tool error `Missing required argument(s): [<names>]` without contacting CoppeliaSim. <!-- CALL-04 -->
5. IF an argument name is not a parameter THEN the system SHALL return an MCP tool error `Unknown argument(s) [<names>]; expected [<params>]` without contacting CoppeliaSim. <!-- CALL-05 -->
6. IF an optional argument is omitted while a later argument is given THEN the system SHALL return an MCP tool error `Optional argument(s) [<names>] must be given because a later one is set`. <!-- CALL-06 -->
7. IF an argument's JSON type does not match its schema `type` THEN the system SHALL return an MCP tool error `Argument '<name>' expected <type>, got <json type>` (integers accepted for `number`; booleans rejected for `integer`/`number`). <!-- CALL-07 -->
8. IF the name is not in the catalog THEN the system SHALL return an MCP tool error `Unknown function '<name>'. Use search_functions.`. <!-- CALL-08 -->
9. IF CoppeliaSim does not answer within `VREP_TIMEOUT` seconds THEN the system SHALL return an MCP tool error `CoppeliaSim not reachable at <host>:<port> (timeout <n>s). Start CoppeliaSim with the ZMQ remote API add-on and retry.` and discard the connection. <!-- CALL-09 -->
10. WHEN a call follows a discarded connection THEN the system SHALL open a new connection. <!-- CALL-10 -->
11. IF CoppeliaSim raises an error for the call THEN the system SHALL return an MCP tool error `CoppeliaSim error in <name>: <message>`. <!-- CALL-11 -->
12. WHILE a call is in flight the system SHALL serialize any other `call_function` invocation until it finishes. <!-- CALL-12 -->

**Independent Test**: With a fake API injected, check positional mapping, validation errors, and serialization. With a real CoppeliaSim, run `sim.getObject` on `/Floor` and read `sim.handle_world`.

---

### P2: Operate the server

**User Story**: As a developer, I want to start the server with one command and see logs without breaking the protocol so that I can plug it into an MCP client.

**Why P2**: Needed for daily use, but the 3 MVP stories can be shown in-memory without it.

**Acceptance Criteria**:

1. WHEN `uv run vrep-mcp` runs THEN the system SHALL serve the 4 tools over stdio and SHALL list exactly `list_namespaces`, `search_functions`, `get_function_schema`, `call_function`. <!-- OPS-01 -->
2. The system SHALL write logs only to stderr and SHALL never write non-protocol bytes to stdout. <!-- OPS-02 -->
3. The system SHALL NOT connect to CoppeliaSim or load the embedding model until a tool needs it. <!-- OPS-03 -->
4. IF a catalog file is missing or not valid JSON at first catalog use THEN the system SHALL return an MCP tool error `Catalog file <path> missing or invalid: <reason>`. <!-- OPS-04 -->

**Independent Test**: Start `uv run vrep-mcp` under an MCP client, list tools, check stdout carries only JSON-RPC.

---

## Edge Cases

- IF `arguments` is omitted for a function with no required params THEN the system SHALL call it with zero positional arguments.
- IF a call returns `None` THEN the system SHALL return JSON `null`.
- IF a return value contains objects JSON cannot represent THEN the system SHALL convert them with `repr()`.
- WHEN the catalog files change content THEN the system SHALL compute a new hash and rebuild the index on the next search (SRCH-06).

**Implicit-requirement sweep:**

- Input validation & bounds: CALL-04..07, SRCH-08..11.
- Failure / partial-failure: CALL-09, CALL-11, OPS-04.
- Idempotency / retry: N/A because each call goes straight to the simulator; the agent retries after CALL-09 and CALL-10 reconnects.
- Auth & rate limits: N/A because the server is local stdio, one client (user decision: no restriction).
- Concurrency / ordering: CALL-12 (the ZMQ REQ socket is not thread-safe).
- Data lifecycle: SRCH-06/07 (cache keyed by hash; old cache files are left in place, see design).
- Observability: OPS-02.
- External-dependency failure: CALL-09/10.
- State-transition integrity: N/A because the server keeps no state machine; simulator state belongs to CoppeliaSim.

---

## Requirement Traceability

| Requirement ID | Story                  | Task       | Status   |
| -------------- | ---------------------- | ---------- | -------- |
| CAT-01         | P1: Read the catalog   | T2         | In Tasks |
| CAT-02         | P1: Read the catalog   | T3         | In Tasks |
| CAT-03         | P1: Read the catalog   | T3         | In Tasks |
| CAT-04         | P1: Read the catalog   | T3         | In Tasks |
| CAT-05         | P1: Read the catalog   | T3         | In Tasks |
| CAT-06         | P1: Read the catalog   | T3         | In Tasks |
| CAT-07         | P1: Read the catalog   | T3         | In Tasks |
| CAT-08         | P1: Read the catalog   | T3         | In Tasks |
| CAT-09         | P1: Read the catalog   | T2         | In Tasks |
| SRCH-01        | P1: Search the catalog | T5         | In Tasks |
| SRCH-02        | P1: Search the catalog | T5         | In Tasks |
| SRCH-03        | P1: Search the catalog | T5         | In Tasks |
| SRCH-04        | P1: Search the catalog | T8         | In Tasks |
| SRCH-05        | P1: Search the catalog | T8         | In Tasks |
| SRCH-06        | P1: Search the catalog | T5         | In Tasks |
| SRCH-07        | P1: Search the catalog | T5         | In Tasks |
| SRCH-08        | P1: Search the catalog | T5         | In Tasks |
| SRCH-09        | P1: Search the catalog | T5         | In Tasks |
| SRCH-10        | P1: Search the catalog | T5         | In Tasks |
| SRCH-11        | P1: Search the catalog | T5         | In Tasks |
| CALL-01        | P1: Execute a function | T4, T6     | In Tasks |
| CALL-02        | P1: Execute a function | T6         | In Tasks |
| CALL-03        | P1: Execute a function | T6         | In Tasks |
| CALL-04        | P1: Execute a function | T4         | In Tasks |
| CALL-05        | P1: Execute a function | T4         | In Tasks |
| CALL-06        | P1: Execute a function | T4         | In Tasks |
| CALL-07        | P1: Execute a function | T4         | In Tasks |
| CALL-08        | P1: Execute a function | T6         | In Tasks |
| CALL-09        | P1: Execute a function | T6         | In Tasks |
| CALL-10        | P1: Execute a function | T6         | In Tasks |
| CALL-11        | P1: Execute a function | T6         | In Tasks |
| CALL-12        | P1: Execute a function | T6         | In Tasks |
| OPS-01         | P2: Operate the server | T1, T7, T9 | In Tasks |
| OPS-02         | P2: Operate the server | T7, T9     | In Tasks |
| OPS-03         | P2: Operate the server | T5, T6     | In Tasks |
| OPS-04         | P2: Operate the server | T2         | In Tasks |

**Coverage:** 36 total, 36 mapped to tasks, 0 unmapped

---

## Success Criteria

- [ ] All 36 requirements are covered by passing tests (offline, plus the CALL e2e smoke against a real CoppeliaSim).
- [ ] SRCH-04 and SRCH-05 pass with the real embedding model.
- [ ] `tools/list` response for the server is under 2,000 tokens.
