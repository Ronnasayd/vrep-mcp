# vrep-mcp

MCP server that exposes the whole CoppeliaSim (V-REP) API through 4 tools, instead of one tool per function. An agent finds a function by searching, reads its schema, then calls it on a running simulator over the ZMQ remote API.

## Tools

| Tool                                                                 | Purpose                                                                                                |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `list_namespaces`                                                    | API namespaces (`sim`, `simUI`, `simROS2`, `simVision`) with function and constant counts              |
| `search_functions(query, max_results=10, namespace=None, kind=None)` | Semantic search over names and descriptions, English or Portuguese. `kind` is `function` or `constant` |
| `get_function_schema(name)`                                          | Signature, docs, return types and JSON `inputSchema` for e.g. `sim.setJointTargetPosition`             |
| `call_function(name, arguments=None)`                                | Runs the function (or reads the constant) on CoppeliaSim. `arguments` maps parameter names to values   |

Typical flow: `search_functions("set joint target position")`, then `get_function_schema("sim.setJointTargetPosition")`, then `call_function("sim.setJointTargetPosition", {"objectHandle": 13, "targetPosition": 1.5})`.

Arguments are validated against the schema before anything reaches the simulator. Simulator errors, timeouts and unknown names come back as MCP tool errors.

## Requirements

- Python 3.11 to 3.14 and [uv](https://docs.astral.sh/uv/)
- CoppeliaSim with the ZMQ remote API server running (default port 23000). It is only needed for `call_function`
- Network access on the first search, to download the embedding model

## Install and run

```bash
uv sync
uv run vrep-mcp   # stdio transport
```

Register it in an MCP client as a stdio server:

```json
{
  "mcpServers": {
    "vrep": {
      "command": "uv",
      "args": ["run", "--project", "/path/to/vrep-mcp", "vrep-mcp"]
    }
  }
}
```

### Run straight from git

No manual install: `uvx` fetches and runs the server from the repository.

```json
{
  "mcpServers": {
    "vrep": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/Ronnasayd/vrep-mcp.git",
        "vrep-mcp"
      ],
      "env": {
        "VREP_DATA_DIR": "${HOME}/develop/personal/vrep-mcp/processed"
      },
      "type": "stdio"
    }
  }
}
```

`VREP_DATA_DIR` is required in this mode. The catalog (`processed/`) is not packaged in the wheel, so it must point to a local clone of this repository. Without it every tool fails with the missing-catalog error. Adjust the repository URL and the clone path to your setup.

Stdout carries JSON-RPC only. Logs go to stderr.

## Configuration

All settings are environment variables.

| Variable         | Default             | Meaning                                                                                                |
| ---------------- | ------------------- | ------------------------------------------------------------------------------------------------------ |
| `VREP_HOST`      | `localhost`         | CoppeliaSim host                                                                                       |
| `VREP_PORT`      | `23000`             | ZMQ remote API port                                                                                    |
| `VREP_TIMEOUT`   | `30`                | Seconds to wait for a simulator reply. On timeout the connection is reset and rebuilt on the next call |
| `VREP_DATA_DIR`  | `<repo>/processed`  | Directory holding the catalog JSON files                                                               |
| `VREP_CACHE_DIR` | `~/.cache/vrep-mcp` | Where the search embeddings are cached                                                                 |

## How it works

- **Catalog**: `processed/*.json` holds the API description, one file per namespace plus constants. Parameter types become JSON Schema types; types with no JSON equivalent (such as `buffer` or `any`) get no `type` and keep `x-vrep-type`.
- **Search**: embeds `<name with camelCase split>: <description>` with `paraphrase-multilingual-MiniLM-L12-v2` (fastembed). The embeddings are cached as `index-<hash>.npy`; the cache key depends on the catalog contents and the text format version, so changing either rebuilds it. The model loads on the first search, not at startup.
- **Bridge**: one lazily created ZMQ client, guarded by a lock so calls never overlap inside the simulator API. Return values are made JSON-safe (tuples to lists, bytes to base64).
- **No call restrictions**: any API function can be called, by design. See [ADR-002](docs/adr/ADR-002-no-call-restrictions.md) and [ADR-001](docs/adr/ADR-001-four-tool-proxy.md).

Source layout:

| File                      | Role                                                  |
| ------------------------- | ----------------------------------------------------- |
| `src/vrep_mcp/server.py`  | FastMCP server and the 4 tools                        |
| `src/vrep_mcp/catalog.py` | Catalog loading, schema building, argument validation |
| `src/vrep_mcp/index.py`   | Embedding search and cache                            |
| `src/vrep_mcp/bridge.py`  | ZMQ client with timeout, reset and lock               |

## Tests

```bash
uv run pytest -q -m "not model and not sim"   # fast, offline
uv run pytest -q -m model                     # real embedding model, downloads it once
uv run pytest -q -m sim                       # needs CoppeliaSim on VREP_HOST:VREP_PORT; skipped when unreachable
uv run pytest -q                              # everything
```

The spec, design and verification report live in [.specs/features/vrep-mcp](.specs/features/vrep-mcp/spec.md).
