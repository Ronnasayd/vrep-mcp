# LESSONS - auto-maintained by scripts/lessons.py

> Machine-owned. Do NOT hand-edit. Changes are overwritten on the next `lessons.py` write.
> Canonical state lives in `.specs/lessons.json`. Edit lessons only via the script.
> promote_threshold=2 distinct features · window_days=45 · quarantine_threshold=2

## Confirmed (load these at Specify/Design)

Corroborated across multiple features. Safe to apply as guidance.

_none_

## Candidates (under observation - do NOT load as guidance yet)

Seen once or not yet corroborated. Tracked, not trusted.

### L-001 - Assert the exact derived cache filename and that bumping the format version changes it; a seeded stale file with an unrelated name passes vacuously

- signal: `surviving_mutant` · recurrence: 1 feature(s) · scope: `cache` · harmful: 0
- features: vrep-mcp
- evidence: src/vrep_mcp/index.py:38 mutant #30 (cache key drops format version) (cache)
- last seen: 2026-10-03T00:21:07Z

### L-002 - Assert the preferred-source value (python signature) as well as the fallback value, so inverting the source choice is caught

- signal: `surviving_mutant` · recurrence: 1 feature(s) · scope: `catalog` · harmful: 0
- features: vrep-mcp
- evidence: src/vrep_mcp/catalog.py:72 mutant #19 (lua fallback always) (catalog)
- last seen: 2026-10-03T00:21:07Z

### L-003 - When a hash/key covers N input files, change each file in turn (or assert the exact digest) so dropping one file from the loop is caught

- signal: `surviving_mutant` · recurrence: 1 feature(s) · scope: `catalog` · harmful: 0
- features: vrep-mcp
- evidence: src/vrep_mcp/catalog.py:109 mutant M19 (hash skips constants.json) (catalog)
- last seen: 2026-10-03T00:27:18Z

### L-004 - Assert a normalization step (strip) against a fixture that actually carries the whitespace, not a value that is already clean

- signal: `surviving_mutant` · recurrence: 1 feature(s) · scope: `catalog` · harmful: 0
- features: vrep-mcp
- evidence: src/vrep_mcp/catalog.py:89 mutant M32 (param docs not stripped) (catalog)
- last seen: 2026-10-03T00:27:18Z

### L-005 - Assert every socket option the bridge sets (send and receive timeouts), not only the one the AC names

- signal: `surviving_mutant` · recurrence: 1 feature(s) · scope: `bridge` · harmful: 0
- features: vrep-mcp
- evidence: src/vrep_mcp/bridge.py:58 mutant M25 (SNDTIMEO dropped) (bridge)
- last seen: 2026-10-03T00:27:18Z

### L-006 - Call the tool without optional args and assert the spec-stated default value, not only explicit values

- signal: `surviving_mutant` · recurrence: 1 feature(s) · scope: `search` · harmful: 0
- features: vrep-mcp
- evidence: src/vrep_mcp/index.py:99 mutant F03 (default max_results 10 changed to 5) (search)
- last seen: 2026-10-03T00:34:49Z

### L-007 - Parametrize routing/dispatch tests over every namespace or branch value, not only the default one

- signal: `surviving_mutant` · recurrence: 1 feature(s) · scope: `bridge` · harmful: 0
- features: vrep-mcp
- evidence: src/vrep_mcp/bridge.py:76 mutant F18 (require namespace hardcoded to sim) (bridge)
- last seen: 2026-10-03T00:34:49Z

### L-008 - Test a spec edge case with a real fixture that exercises it (all-optional params, empty arguments), not a trivially empty one

- signal: `surviving_mutant` · recurrence: 1 feature(s) · scope: `catalog` · harmful: 0
- features: vrep-mcp
- evidence: src/vrep_mcp/catalog.py:209 mutant F19 (no-arg default index -1 changed to 0) (catalog)
- last seen: 2026-10-03T00:34:49Z

## Quarantined (failed when applied - ignore)

A confirmed lesson that recurred alongside failure. Kept for the maintainer to review.

_none_
