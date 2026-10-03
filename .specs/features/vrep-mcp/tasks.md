# vrep-mcp Tasks

## Execution Protocol (MANDATORY -- do not skip)

Implement these tasks with the `tlc-spec-driven` skill: **activate it by name and follow its Execute flow and Critical Rules.** Do not search for skill files by filesystem path. The skill is the source of truth for the full flow (per-task cycle, sub-agent delegation, adequacy review, Verifier, discrimination sensor).

**If the skill cannot be activated, STOP and tell the user - do not proceed without it.**

---

**Design**: `.specs/features/vrep-mcp/design.md`
**Status**: Approved
**Execution tools (user choice)**: context7, serena, sub-agents (2 batches: Phase 1 / Phases 2-3), plus any other tool needed

---

## Test Coverage Matrix

> Generated from codebase, project guidelines, and spec - confirm before Execute. Guidelines found: `AGENTS.md` ("never assume the code is correct without tests"; the Playwright rule applies to UI only, and this feature has none), `pyproject.toml` (`[tool.pytest.ini_options] testpaths = ["tests"]`), draft `tests/test_catalog.py`. No coverage threshold configured, so strong defaults apply.

| Code Layer                        | Required Test Type                           | Coverage Expectation                                                                  | Location Pattern               | Run Command                              |
| --------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------ | ---------------------------------------- |
| Domain: catalog (`catalog.py`)    | unit                                         | All branches; 1:1 to CAT/CALL-04..08 ACs; Lua fallback, misaligned docs, missing file | `tests/test_catalog.py`        | `uv run pytest -q tests/test_catalog.py` |
| Domain: search (`index.py`)       | unit                                         | All branches with fake embedder; SRCH-01..03, 06..11                                  | `tests/test_index.py`          | `uv run pytest -q tests/test_index.py`   |
| Adapter: ZMQ bridge (`bridge.py`) | unit                                         | Fake client: success, sim error, timeout→reset→reconnect, lock, serialization         | `tests/test_bridge.py`         | `uv run pytest -q tests/test_bridge.py`  |
| MCP layer (`server.py`)           | integration                                  | Every tool via in-memory `fastmcp.Client`: happy + error path per tool                | `tests/test_server.py`         | `uv run pytest -q tests/test_server.py`  |
| Real model search quality         | integration (marker `model`)                 | SRCH-04, SRCH-05 with the real embedding model                                        | `tests/test_search_quality.py` | `uv run pytest -q -m model`              |
| stdio process                     | e2e                                          | OPS-01/02 by spawning `uv run vrep-mcp`                                               | `tests/test_stdio.py`          | `uv run pytest -q tests/test_stdio.py`   |
| Real CoppeliaSim                  | e2e (marker `sim`, skipped when unreachable) | CALL-01, CALL-03 against a live simulator                                             | `tests/test_sim_e2e.py`        | `uv run pytest -q -m sim`                |
| Config (`pyproject.toml`)         | none                                         | build gate only                                                                       | -                              | build gate only                          |

## Gate Check Commands

> Generated from codebase - confirm before Execute.

| Gate Level | When to Use                                 | Command                                                                                                 |
| ---------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Quick      | After tasks with unit tests only            | `uv run pytest -q -m "not model and not sim"`                                                           |
| Full       | After tasks with integration/e2e tests      | `uv run pytest -q -m "not sim"`                                                                         |
| Build      | After phase completion or config-only tasks | `uv sync --locked && uv run python -m compileall -q src && uv run pytest -q -m "not model and not sim"` |

---

## Execution Plan

Phases are ordered and run sequentially - each phase completes before the next begins, and tasks within a phase execute in order.

### Phase 1: Catalog foundation

```
T1 → T2 → T3 → T4
```

### Phase 2: Search, bridge, server

```
T5 → T6 → T7
```

### Phase 3: Real-world verification

```
T8 → T9 → T10
```

---

## Task Breakdown

### T1: Configure dependencies and test markers

**What**: Add `fastembed` and `numpy` (pinned ranges) to `pyproject.toml`, register pytest markers `model` and `sim`, regenerate `uv.lock`.
**Where**: `pyproject.toml`
**Depends on**: None
**Reuses**: `../mcp-manager/pyproject.toml` dependency style
**Requirement**: OPS-01

**Tools**:

- MCP: NONE
- Skill: NONE

**Done when**:

- [ ] `uv sync --locked` succeeds with the new `uv.lock` committed
- [ ] `uv run pytest --markers` lists `model` and `sim`
- [ ] Gate check passes: `uv sync --locked && uv run python -m compileall -q src && uv run pytest -q -m "not model and not sim"`

**Tests**: none
**Gate**: build

**Commit**: `build(deps): add fastembed, numpy and pytest markers`

---

### T2: Catalog loading with fallbacks and hash

**What**: `VrepError`, `Entry` normalization (`entries`, `get`, `list_namespaces`, `catalog_hash`) with Lua fallback for missing `python_raw`, aligned-only `param_docs`, and the OPS-04 error.
**Where**: `src/vrep_mcp/catalog.py`
**Depends on**: T1
**Reuses**: draft `entries`, `list_namespaces`
**Requirement**: CAT-01, CAT-07 (entry part), CAT-09, CALL-08, OPS-04

**Tools**:

- MCP: NONE
- Skill: NONE

**Done when**:

- [x] `list_namespaces()` returns the counts in CAT-01 exactly
- [x] `get("sim.serialRead")` carries `lua` params and `lua_raw` signature
- [x] Unknown name raises `VrepError` with the CAT-09 message
- [x] A missing or corrupt catalog file (via `VREP_DATA_DIR` tmp dir) raises the OPS-04 message
- [x] `catalog_hash()` changes when one file's bytes change
- [x] Gate check passes: `uv run pytest -q -m "not model and not sim"`
- [x] Test count: ≥ 6 tests in `tests/test_catalog.py` pass

**Tests**: unit
**Gate**: quick

**Status**: done

**Commit**: `feat(catalog): load processed catalog with lua and doc fallbacks`

---

### T3: Schema builder

**What**: `schema(name)` returning the CAT-02 shape for functions and the CAT-08 shape for constants, with type mapping, `x-vrep-type`, required set, and aligned descriptions.
**Where**: `src/vrep_mcp/catalog.py` (modify)
**Depends on**: T2
**Reuses**: draft `schema`, `_is_optional`
**Requirement**: CAT-02, CAT-03, CAT-04, CAT-05, CAT-06, CAT-07, CAT-08

**Tools**:

- MCP: NONE
- Skill: NONE

**Done when**:

- [x] `sim.setJointTargetPosition` required = `["objectHandle","targetPosition"]`, `targetPosition.type == "number"`
- [x] A `buffer`/`any`-typed param has no `type` key and keeps `x-vrep-type`
- [x] A function with misaligned definitions has no property `description`; an aligned one has them
- [x] `sim.serialRead` required excludes `closingString` and `timeout` (Lua fallback)
- [x] `sim.handle_world` returns `{kind:"constant", namespace:"sim", type:"int"}`
- [x] Gate check passes: `uv run pytest -q -m "not model and not sim"`
- [x] Test count: ≥ 11 tests in `tests/test_catalog.py` pass

**Tests**: unit
**Gate**: quick

**Status**: done

**Commit**: `feat(catalog): build JSON input schemas from catalog entries`

---

### T4: Argument validation and positional mapping

**What**: `to_positional(name, arguments)` enforcing CALL-04..07 and mapping named args to the positional list truncated after the last given argument.
**Where**: `src/vrep_mcp/catalog.py` (modify)
**Depends on**: T3
**Reuses**: draft `build_args`; type check idea from `../mcp-manager/src/tools/call_tool.py`
**Requirement**: CALL-01 (mapping), CALL-04, CALL-05, CALL-06, CALL-07

**Tools**:

- MCP: NONE
- Skill: NONE

**Done when**:

- [x] Each of the 4 error messages matches the spec text exactly
- [x] `int` accepted for `number`; `bool` rejected for `integer` and `number`; untyped params accept any JSON
- [x] `{"objectHandle":5,"targetPosition":1.5}` → `[5, 1.5]`; empty arguments for a no-param function → `[]`
- [x] Gate check passes: `uv run pytest -q -m "not model and not sim"`
- [x] Test count: ≥ 17 tests in `tests/test_catalog.py` pass

**Tests**: unit
**Gate**: quick

**Status**: done

**Commit**: `feat(catalog): validate and map named arguments to positional`

---

### T5: Embedding search with hash-keyed cache

**What**: `index.search` with input validation, namespace/kind filters, cosine score ×100, and lazy `.npy` cache at `VREP_CACHE_DIR/index-<hash16>.npy`.
**Where**: `src/vrep_mcp/index.py`
**Depends on**: None (Phase 1 complete)
**Reuses**: mcp-manager model id + `"<name>: <description>"` text format
**Requirement**: SRCH-01, SRCH-02, SRCH-03, SRCH-06, SRCH-07, SRCH-08, SRCH-09, SRCH-10, SRCH-11, OPS-03 (model lazy)

**Tools**:

- MCP: `context7` (fastembed `TextEmbedding` API)
- Skill: NONE

**Done when**:

- [x] With a fake embedder: results sorted desc, ≤ `max_results`, fields per SRCH-01, description ≤ 200 chars
- [x] Filters return only the matching namespace / kind
- [x] First search writes the cache file; a second search with a fresh module state loads it and calls the embedder only for the query
- [x] SRCH-08..11 messages match exactly
- [x] Importing `vrep_mcp.index` does not instantiate the embedder
- [x] Gate check passes: `uv run pytest -q -m "not model and not sim"`
- [x] Test count: ≥ 9 tests in `tests/test_index.py` pass

**Tests**: unit
**Gate**: quick

**Status**: done

**Commit**: `feat(index): add embedding search with on-disk cache`

---

### T6: ZMQ bridge with timeout, reset, and lock

**What**: `bridge.call` holding a module lock, lazy `RemoteAPIClient(host, port, verbose=0)` with `RCVTIMEO`/`LINGER`, reset on timeout, error wrapping, and `jsonable`.
**Where**: `src/vrep_mcp/bridge.py`
**Depends on**: T5
**Reuses**: draft `_api`, `call`, `jsonable` from `catalog.py` (moved out)
**Requirement**: CALL-01, CALL-02, CALL-03, CALL-08, CALL-09, CALL-10, CALL-11, CALL-12, OPS-03 (lazy connect)

**Tools**:

- MCP: NONE
- Skill: NONE

**Done when**:

- [ ] Fake API: positional invocation, tuple→list, bytes→base64, `None`→`null`, constant read ignores `arguments`
- [ ] Fake client raising `zmq.Again` → CALL-09 message; next call builds a new client (CALL-10)
- [ ] Fake API raising `Exception("boom")` → `CoppeliaSim error in <name>: boom`; missing attribute → the "not available" message
- [ ] Two threads calling concurrently never overlap inside the API (CALL-12)
- [ ] Invalid arguments raise before the client factory is called
- [ ] Draft ZMQ code removed from `catalog.py`
- [ ] Gate check passes: `uv run pytest -q -m "not model and not sim"`
- [ ] Test count: ≥ 9 tests in `tests/test_bridge.py` pass

**Tests**: unit
**Gate**: quick

**Commit**: `feat(bridge): add ZMQ bridge with timeout, reconnect and lock`

---

### T7: FastMCP server with the 4 tools

**What**: `server.py` exposing `list_namespaces`, `search_functions(query, max_results, namespace, kind)`, `get_function_schema`, `call_function`, mapping `VrepError` to `ToolError`, and logging to stderr.
**Where**: `src/vrep_mcp/server.py` (modify)
**Depends on**: T6
**Reuses**: draft `server.py`
**Requirement**: OPS-01, OPS-02, CAT-01, CAT-02, CAT-09, SRCH-01, CALL-04, CALL-09

**Tools**:

- MCP: `context7` (fastmcp 2.x `ToolError`, in-memory `Client`)
- Skill: NONE

**Done when**:

- [ ] In-memory `fastmcp.Client` lists exactly the 4 tool names
- [ ] One happy path and one error path per tool return the spec payload / message (fake embedder and fake API injected)
- [ ] Gate check passes: `uv run pytest -q -m "not sim"`
- [ ] Test count: ≥ 8 tests in `tests/test_server.py` pass

**Tests**: integration
**Gate**: full

**Commit**: `feat(server): expose catalog, search and call as 4 MCP tools`

---

### T8: Real-model search quality check

**What**: Marker-`model` tests asserting SRCH-04 and SRCH-05 against the real multilingual model.
**Where**: `tests/test_search_quality.py`
**Depends on**: None (Phase 2 complete)
**Reuses**: `index.search`
**Requirement**: SRCH-04, SRCH-05

**Tools**:

- MCP: NONE
- Skill: NONE

**Done when**:

- [ ] `uv run pytest -q -m model` passes (downloads the model once)
- [ ] Both queries rank `sim.setJointTargetPosition` in the top 5
- [ ] Gate check passes: `uv run pytest -q -m "not sim"`
- [ ] Test count: 2 tests in `tests/test_search_quality.py` pass

**Tests**: integration
**Gate**: full

**Commit**: `test(index): check multilingual search quality with real model`

---

### T9: stdio process smoke test

**What**: Spawn `uv run vrep-mcp` through `fastmcp.Client` stdio transport, list tools, call `get_function_schema`, assert the session works (stdout stays pure JSON-RPC).
**Where**: `tests/test_stdio.py`
**Depends on**: T8
**Reuses**: `[project.scripts] vrep-mcp`
**Requirement**: OPS-01, OPS-02

**Tools**:

- MCP: NONE
- Skill: NONE

**Done when**:

- [ ] Subprocess session lists the 4 tools and returns the `sim.getObject` schema
- [ ] Session also succeeds with `VERBOSE=2` in the environment (client stdout printing suppressed)
- [ ] Gate check passes: `uv run pytest -q -m "not sim"`
- [ ] Test count: 2 tests in `tests/test_stdio.py` pass

**Tests**: e2e
**Gate**: full

**Commit**: `test(server): add stdio subprocess smoke test`

---

### T10: Live CoppeliaSim e2e

**What**: Marker-`sim` tests (skipped when `localhost:23000` is unreachable) calling `sim.getSimulationState`, `sim.getObject` on `/Floor`, and reading `sim.handle_world` through `call_function`.
**Where**: `tests/test_sim_e2e.py`
**Depends on**: T9
**Reuses**: `bridge.call`
**Requirement**: CALL-01, CALL-02, CALL-03

**Tools**:

- MCP: NONE
- Skill: NONE

**Done when**:

- [ ] With CoppeliaSim running (default scene): 3 tests pass via `uv run pytest -q -m sim`
- [ ] Without CoppeliaSim: the 3 tests report as skipped, not failed
- [ ] Gate check passes: `uv run pytest -q -m "not model and not sim"`
- [ ] Test count: 3 tests in `tests/test_sim_e2e.py` (pass or skip)

**Tests**: e2e
**Gate**: full

**Commit**: `test(bridge): add live CoppeliaSim e2e checks`

---

## Phase Execution Map

```
Phase 1 → Phase 2 → Phase 3

Phase 1:  T1 ------→ T2 ------→ T3 ------→ T4
Phase 2:  T5 ------→ T6 ------→ T7
Phase 3:  T8 ------→ T9 ------→ T10
```

---

## Task Granularity Check

| Task                       | Scope                                                | Status          |
| -------------------------- | ---------------------------------------------------- | --------------- |
| T1: Dependencies + markers | 1 config file                                        | ✅ Granular     |
| T2: Catalog loading        | 1 function group in 1 file                           | ✅ Granular     |
| T3: Schema builder         | 1 function                                           | ✅ Granular     |
| T4: Arg validation/mapping | 1 function                                           | ✅ Granular     |
| T5: Search + cache         | 1 module, cohesive (search needs its cache)          | ⚠️ OK, cohesive |
| T6: ZMQ bridge             | 1 module, cohesive (call + its connection lifecycle) | ⚠️ OK, cohesive |
| T7: MCP server             | 1 file, 4 thin wrappers                              | ✅ Granular     |
| T8: Search quality test    | 1 test file                                          | ✅ Granular     |
| T9: stdio smoke            | 1 test file                                          | ✅ Granular     |
| T10: Live sim e2e          | 1 test file                                          | ✅ Granular     |

## Diagram-Definition Cross-Check

| Task | Depends On (task body)  | Diagram Shows    | Status   |
| ---- | ----------------------- | ---------------- | -------- |
| T1   | None                    | start of Phase 1 | ✅ Match |
| T2   | T1                      | T1 → T2          | ✅ Match |
| T3   | T2                      | T2 → T3          | ✅ Match |
| T4   | T3                      | T3 → T4          | ✅ Match |
| T5   | None (Phase 1 complete) | start of Phase 2 | ✅ Match |
| T6   | T5                      | T5 → T6          | ✅ Match |
| T7   | T6                      | T6 → T7          | ✅ Match |
| T8   | None (Phase 2 complete) | start of Phase 3 | ✅ Match |
| T9   | T8                      | T8 → T9          | ✅ Match |
| T10  | T9                      | T9 → T10         | ✅ Match |

## Test Co-location Validation

| Task | Code Layer Created/Modified | Matrix Requires | Task Says   | Status |
| ---- | --------------------------- | --------------- | ----------- | ------ |
| T1   | Config                      | none            | none        | ✅ OK  |
| T2   | Domain: catalog             | unit            | unit        | ✅ OK  |
| T3   | Domain: catalog             | unit            | unit        | ✅ OK  |
| T4   | Domain: catalog             | unit            | unit        | ✅ OK  |
| T5   | Domain: search              | unit            | unit        | ✅ OK  |
| T6   | Adapter: ZMQ bridge         | unit            | unit        | ✅ OK  |
| T7   | MCP layer                   | integration     | integration | ✅ OK  |
| T8   | Real model search quality   | integration     | integration | ✅ OK  |
| T9   | stdio process               | e2e             | e2e         | ✅ OK  |
| T10  | Real CoppeliaSim            | e2e             | e2e         | ✅ OK  |

## Requirement Coverage

All 36 spec IDs map to at least one task: CAT-01..09 → T2/T3; SRCH-01..03, 06..11 → T5; SRCH-04/05 → T8; CALL-01, 04..07 → T4; CALL-01..03, 08..12 → T6; OPS-01 → T1/T7/T9; OPS-02 → T7/T9; OPS-03 → T5/T6; OPS-04 → T2.
