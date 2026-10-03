# ADR-002 – No restriction on callable functions

> **Date:** 2026-10-02
> **Status:** Accepted
> **Deciders:** Project owner (Ronnasayd)

## Context

`call_function` can run any catalog function, including destructive ones: quitting the simulator, removing objects, overwriting scenes, and running arbitrary script code. A reader would expect a denylist, a read-only mode, or a confirmation step. vrep-mcp runs locally over stdio for one user who controls both the agent and the simulator.

## Decision

Every catalog function is callable, with no denylist, no read-only mode, and no confirmation. The goal is to reach "every possible function" with the least machinery. Scene safety stays with the user (save scenes, run disposable simulator instances).

## Considered Alternatives

| Alternative                                            | Pros                                                        | Cons                                                                                        |
| ------------------------------------------------------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Allow everything (chosen)**                          | Full API reach; no list to keep in sync with ~575 functions | An agent mistake can destroy unsaved scene state or close the simulator                     |
| Configurable denylist with destructive defaults        | Blocks the most dangerous calls                             | The list needs upkeep as the API grows; the blocked calls are often exactly the ones needed |
| Optional read-only mode (`get*`/`read*`/`check*` only) | Safe exploration mode                                       | Name-prefix heuristics misclassify functions; extra configuration surface                   |

## Consequences

- Unsaved simulator state can be lost by a single agent call.
- Before exposing the server beyond a single local user (HTTP transport, shared machines), revisit this decision. It rests on the local, single-user setup.
- Do not add a safety layer as a "fix" without superseding this ADR.

## Related ADRs

- ADR-001 – Expose the CoppeliaSim API through a 4-tool proxy.
