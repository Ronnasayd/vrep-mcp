# vrep-mcp Validation

**Date**: 2026-10-02
**Spec**: `.specs/features/vrep-mcp/spec.md` (SRCH indexed text = camelCase-split, deliberate amendment, c7b4429)
**Diff range**: a7e205c..HEAD (36db45c) plus root
**Verifier**: fresh independent sub-agent, iteration 3 of 3 (final; author != verifier)
**Verdict**: FAIL (non-equivalent survivors F03, F18, F19, F16, F30, F31; escalate to user)

---

## Task Completion

| Task  | Status                                    | Notes                                                                                                                                                         |
| ----- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| T1    | Done                                      | tasks.md:92 `Status: done` (bookkeeping fixed in ed911ac)                                                                                                     |
| T2-T9 | Done                                      | `Status: done` in tasks.md                                                                                                                                    |
| T10   | Done in tasks.md, UNVERIFIED-skipped here | CoppeliaSim unreachable at localhost:23000; `pytest -m sim` = 3 skipped (tests/test_sim_e2e.py:36,42,49). CALL-01/CALL-03 against live simulator NOT verified |

Ship risks from iter 2 resolved: `processed/*.json` and `src/vrep_mcp/__init__.py` now tracked (36db45c, `git ls-files` confirms).

---

## Spec-Anchored Acceptance Criteria

Tests: C=`tests/test_catalog.py`, I=`tests/test_index.py`, B=`tests/test_bridge.py`, S=`tests/test_server.py`, ST=`tests/test_stdio.py`, Q=`tests/test_search_quality.py`.

| AC      | Spec-defined outcome                                                                         | `file:line` + assertion                                           | Result                                                                      |
| ------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------- |
| CAT-01  | 4 ns in order, 323/399,146/0,61/0,46/0                                                       | C:9-14 `list_namespaces() == [...]`; S:101-107                    | PASS                                                                        |
| CAT-02  | keys name,kind,namespace,signature,description,url,returns,inputSchema; props in param order | C:70-86 `{...} <= set(s)`, `list(properties) == [...]`; S:131-132 | PASS for keys; `url`/`returns` VALUES unasserted (mutants F30, F31 survive) |
| CAT-03  | required == [objectHandle, targetPosition]                                                   | C:90 `s["required"] == [...]`                                     | PASS                                                                        |
| CAT-04  | type map + x-vrep-type; unmapped = no type                                                   | C:91-96, C:98-101, C:252-258                                      | PASS                                                                        |
| CAT-05  | aligned defs -> property description                                                         | C:111 `== "handle of a scene object."`; C:261-265 strip           | PASS                                                                        |
| CAT-06  | misaligned -> no descriptions                                                                | C:104-106                                                         | PASS                                                                        |
| CAT-07  | no python_raw -> lua params + lua_raw signature                                              | C:17-26, C:114-116                                                | PASS                                                                        |
| CAT-08  | name, kind=constant, namespace=sim, type=int                                                 | C:119-125 exact dict                                              | PASS                                                                        |
| CAT-09  | `Unknown function '<name>'. Use search_functions.`                                           | C:29-32; S:135-138                                                | PASS                                                                        |
| SRCH-01 | <= max_results (default 10), desc-sorted, 5 fields, desc <= 200, score 0-100                 | I:49-60, I:74-82, I:200-210                                       | PASS except DEFAULT 10 never asserted (F03 survives)                        |
| SRCH-02 | namespace filter                                                                             | I:85-89                                                           | PASS                                                                        |
| SRCH-03 | kind filter                                                                                  | I:92-97; S:110-119                                                | PASS                                                                        |
| SRCH-04 | top 5 incl. setJointTargetPosition (real model)                                              | Q:26-29 `EXPECTED in names`                                       | PASS (model run)                                                            |
| SRCH-05 | same, Portuguese                                                                             | Q:26-29                                                           | PASS (model run)                                                            |
| SRCH-06 | embed 975, write `index-<sha256(hash:version)[:16]>.npy`                                     | I:100-107, I:122-128, I:131-145, I:158-168 (all 5 files)          | PASS                                                                        |
| SRCH-07 | cached file loaded, no re-embed                                                              | I:148-155 `fake.calls == [["joint"]]`                             | PASS                                                                        |
| SRCH-08 | `query must not be empty`                                                                    | I:174-175, I:191; S:122-125                                       | PASS                                                                        |
| SRCH-09 | `max_results must be between 1 and 50`                                                       | I:176-177, I:195-197                                              | PASS                                                                        |
| SRCH-10 | `Unknown namespace 'foo'. Valid: sim, simUI, simROS2, simVision`                             | I:178-181                                                         | PASS                                                                        |
| SRCH-11 | `kind must be 'function' or 'constant'`                                                      | I:182                                                             | PASS                                                                        |
| CALL-01 | `require(ns).<method>(*positional)`                                                          | B:87-97 (`required == "sim"`, calls tuple); C:138-141             | PARTIAL: only namespace `sim` exercised (F18 survives); live-sim UNVERIFIED |
| CALL-02 | tuple->array, bytes/bytearray->base64                                                        | B:129-154                                                         | PASS                                                                        |
| CALL-03 | constant value, args ignored                                                                 | B:157-161 `== -6`, `calls == []`                                  | PASS offline; live UNVERIFIED                                               |
| CALL-04 | `Missing required argument(s): [...]`, no contact                                            | C:148; B:216-221                                                  | PASS                                                                        |
| CALL-05 | `Unknown argument(s) [...]; expected [...]`                                                  | C:153-160                                                         | PASS                                                                        |
| CALL-06 | `Optional argument(s) [...] must be given...`                                                | C:179-193                                                         | PASS                                                                        |
| CALL-07 | `Argument '<n>' expected <t>, got <j>`; int ok for number; bool rejected                     | C:169, 196-233                                                    | PASS                                                                        |
| CALL-08 | unknown name error                                                                           | B:224-229                                                         | PASS                                                                        |
| CALL-09 | exact message + connection discarded                                                         | B:164-178; S:157-171                                              | PASS                                                                        |
| CALL-10 | new connection after discard                                                                 | B:181-192                                                         | PASS                                                                        |
| CALL-11 | `CoppeliaSim error in <name>: <message>`                                                     | B:195-203                                                         | PASS                                                                        |
| CALL-12 | serialized                                                                                   | B:232-253 `state["max"] == 1`                                     | PASS                                                                        |
| OPS-01  | exactly 4 tools over stdio                                                                   | ST:26-39; S:92-95                                                 | PASS                                                                        |
| OPS-02  | stdout only JSON-RPC                                                                         | ST:42-99                                                          | PASS                                                                        |
| OPS-03  | no connect/model load until needed                                                           | I:235-245; B:87-93, 123-126                                       | PASS                                                                        |
| OPS-04  | `Catalog file <path> missing or invalid: <reason>`                                           | C:35-50; I:227-232                                                | PASS                                                                        |

**Edge cases**: omitted args -> zero positional: C:134 only with a function that has NO params; the all-optional case (10 shipped functions, e.g. `sim.moduleEntry`) is unasserted (F19 survives). `None` -> null B:129-134. non-JSON -> repr B:147-154. changed catalog -> new hash/rebuild C:53-57 (5 files), I:158-168.
**Success criteria**: tools/list measured read-only = 2451 bytes (~612 tokens) < 2000 tokens; no regression test pins it.

**Status**: all 36 ACs have file:line evidence; CAT-02 values, SRCH-01 default, CALL-01 namespace routing, and the omitted-args edge case have weak assertions (found by sensor).

---

## Discrimination Sensor

Scratch: temp git worktree under session scratchpad, venv python + PYTHONPATH to scratch `src`, offline suite minus stdio (95 tests, ~2s/mutant). Worktree removed and pruned. No `git stash`.

| #    | File:line      | Mutation                                          | Result                                                                                                                 |
| ---- | -------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| M19  | catalog.py:109 | hash loop skips constants.json                    | Killed (prior survivor)                                                                                                |
| M32  | catalog.py:89  | param-doc `.strip()` removed                      | Killed (prior survivor)                                                                                                |
| M25  | bridge.py:58   | SNDTIMEO setsockopt removed                       | Killed (prior survivor)                                                                                                |
| F01  | server.py:59   | namespace/kind args swapped                       | Killed                                                                                                                 |
| F02  | server.py:77   | `arguments` dropped                               | Killed                                                                                                                 |
| F03a | server.py:49   | tool default `max_results` 10 -> 5                | SURVIVED (SRCH-01 default 10 untested)                                                                                 |
| F03b | index.py:99    | index default `max_results` 10 -> 5               | SURVIVED (same)                                                                                                        |
| F04  | index.py:18    | MAX 50 -> 51                                      | Killed                                                                                                                 |
| F05  | index.py:18    | MIN 1 -> 0                                        | Killed                                                                                                                 |
| F06  | index.py:73    | `strip()` dropped in empty check                  | Killed                                                                                                                 |
| F07  | index.py:81    | Valid join `', '` -> `','`                        | Killed                                                                                                                 |
| F08  | catalog.py:126 | constants count uses function kind                | Killed                                                                                                                 |
| F09  | catalog.py:224 | no truncation after last given                    | Killed                                                                                                                 |
| F10  | bridge.py:26   | jsonable no JSON roundtrip                        | Killed                                                                                                                 |
| F11  | bridge.py:84   | constants invoked as functions                    | Killed                                                                                                                 |
| F12  | bridge.py:108  | `from exc` -> `from None`                         | SURVIVED, equivalent (exception chaining only, no message/behavior change)                                             |
| F13  | bridge.py:105  | `except VrepError: raise` removed                 | Killed                                                                                                                 |
| F14  | bridge.py:66   | `_client` not cleared in reset                    | Killed                                                                                                                 |
| F15  | bridge.py:69   | `context.term()` removed                          | Killed                                                                                                                 |
| F16  | catalog.py:135 | optional regex `\b` dropped                       | SURVIVED, real: changes `required` of `simUI.addTreeItem` (param `id`) on shipped data; untested                       |
| F17  | catalog.py:144 | constant schema type -> "float"                   | Killed                                                                                                                 |
| F18  | bridge.py:76   | `require(entry["namespace"])` -> `require("sim")` | SURVIVED, real: CALL-01 namespace routing untested for simUI/simROS2/simVision                                         |
| F19  | catalog.py:209 | `default=-1` -> `0`                               | SURVIVED, real: 10 shipped all-optional functions called with empty args would raise KeyError; spec edge case untested |
| F20  | catalog.py:65  | constant description emptied                      | SURVIVED, spec-precision (spec defines no constant description; affects search text)                                   |
| F21  | index.py:118   | score `round(,2)` -> `round(,0)`                  | SURVIVED, equivalent per spec (precision undefined; spec-precision note)                                               |
| F22  | index.py:56    | `mkdir(parents=True)` -> False                    | SURVIVED, minor (only deep nonexistent VREP_CACHE_DIR; untested)                                                       |
| F23  | bridge.py:16   | default port 23001                                | Killed                                                                                                                 |
| F24  | bridge.py:17   | default timeout 31                                | Killed                                                                                                                 |
| F25  | bridge.py:18   | MS_PER_S 100                                      | Killed                                                                                                                 |
| F26  | bridge.py:59   | LINGER 1                                          | Killed                                                                                                                 |
| F27  | catalog.py:41  | `ValueError` not caught                           | Killed                                                                                                                 |
| F28  | server.py:66   | get_function_schema returns raw entry             | Killed                                                                                                                 |
| F29  | catalog.py:149 | `x-vrep-type` = param_name                        | Killed                                                                                                                 |
| F30  | catalog.py:160 | schema `returns` -> []                            | SURVIVED, real: CAT-02 `returns` value unasserted                                                                      |
| F31  | catalog.py:161 | schema `url` -> None                              | SURVIVED, real: CAT-02 `url` value unasserted                                                                          |
| F33  | bridge.py:102  | `:g` format dropped (`5.0s`)                      | Killed                                                                                                                 |

(F32 pattern matched twice, not run.)

**Sensor depth**: P0-style manual run, 37 effective mutants (3 prior + 34 fresh).
**Result**: 28/37 killed; 9 survived: 2 equivalent (F12, F21), 1 spec-precision (F20), 6 real non-equivalent (F03a/b counted as one, F16, F18, F19, F22 minor, F30, F31). FAIL.

Isolation: `git status --porcelain` before == after (10 entries identical; baseline file lacked trailing newline only). Real tree untouched.

---

## Code Quality

| Principle                             | Status                                                                        |
| ------------------------------------- | ----------------------------------------------------------------------------- |
| Minimum code / no scope creep         | Yes                                                                           |
| Matches patterns                      | Yes                                                                           |
| Spec-anchored outcome check           | Yes for error-message ACs (exact strings asserted)                            |
| Every test maps to a spec requirement | Yes                                                                           |
| Guidelines                            | AGENTS.md ("never assume correct without tests"); Playwright rule N/A (no UI) |

---

## Gate Check

- **Gate command**: `pytest -q -m "not sim"` (venv python, full incl. model + stdio)
- **Result**: 99 passed, 0 failed, 3 deselected (sim)
- **Test count before feature (a7e205c)**: 0
- **Test count after**: 102 collected (99 run + 3 sim)
- **Skipped**: 3 `sim` tests (test_sim_e2e.py:36,42,49): CoppeliaSim unreachable at localhost:23000. T10 live-sim UNVERIFIED-skipped.
- **Failures**: none

---

## Fix Plans (ranked)

1. (Major) CALL-01: add bridge test with a non-`sim` function (e.g. `simUI.*`) asserting `client.required == "simUI"` (kills F18).
2. (Major) SRCH-01: call `index.search("handle")` and server `search_functions` without `max_results`, assert `len == 10` (kills F03a/b).
3. (Major) Edge case: `to_positional("sim.moduleEntry", {})` -> `[]` (kills F19).
4. (Minor) CAT-02: assert `url` and `returns` values for `sim.getObject` (kills F30, F31).
5. (Minor) Assert `required` for `simUI.addTreeItem` excludes/includes `id` correctly (kills F16).
6. (Minor) Cache dir nested nonexistent path test (F22); constant description in search text (F20, spec-precision).

---

## Requirement Traceability Update

| Requirement                                         | Previous | New                                                |
| --------------------------------------------------- | -------- | -------------------------------------------------- |
| CAT-01,03..09, SRCH-02..11, CALL-02..12, OPS-01..04 | In Tasks | Verified                                           |
| CAT-02                                              | In Tasks | Needs Fix (url/returns values)                     |
| SRCH-01                                             | In Tasks | Needs Fix (default 10)                             |
| CALL-01                                             | In Tasks | Needs Fix (namespace routing); live-sim UNVERIFIED |
| CALL-03                                             | In Tasks | Verified offline; live UNVERIFIED                  |

---

## Summary

**Overall**: Not Ready (iteration 3 of 3 exhausted; escalate to user)

**Spec-anchored check**: 36/36 ACs with file:line; 4 weak assertions (CAT-02 values, SRCH-01 default, CALL-01 namespace, omitted-args edge)
**Sensor**: 28/37 killed; 6 real survivors, 2 equivalent, 1 spec-precision
**Gate**: 99 passed, 0 failed, 3 sim skipped (T10 UNVERIFIED-skipped)

**What works**: all 3 prior survivors killed; processed/ and `__init__.py` tracked; real-model SRCH-04/05 pass; stdio stdout clean; tools/list ~612 tokens.

**Next steps**: user decides: add the 4 small tests above (cheap, no src change) or accept residual risk; run `pytest -m sim` against a live CoppeliaSim for T10.
