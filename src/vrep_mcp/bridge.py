"""ZMQ bridge to CoppeliaSim: lazy connection, receive timeout, reset, one call at a time."""

from __future__ import annotations

import base64
import json
import os
import threading
from typing import Any

import zmq

from . import catalog

DEFAULT_HOST = "localhost"
DEFAULT_PORT = "23000"
DEFAULT_TIMEOUT_S = "30"
MS_PER_S = 1000

# invariant: the client wraps one REQ socket, which is not thread-safe (CALL-12)
_lock = threading.Lock()
_client: Any = None


def jsonable(value: Any) -> Any:
    return json.loads(
        json.dumps(
            value,
            default=lambda o: (
                base64.b64encode(o).decode()
                if isinstance(o, (bytes, bytearray))
                else repr(o)
            ),
        )
    )


def _host_port() -> tuple[str, int]:
    return (
        os.environ.get("VREP_HOST", DEFAULT_HOST),
        int(os.environ.get("VREP_PORT", DEFAULT_PORT)),
    )


def _timeout_s() -> float:
    return float(os.environ.get("VREP_TIMEOUT", DEFAULT_TIMEOUT_S))


def _new_client() -> Any:
    from coppeliasim_zmqremoteapi_client import RemoteAPIClient

    host, port = _host_port()
    # hazard: verbose=0 because the client prints to stdout, which carries JSON-RPC (OPS-02)
    # hazard: the constructor also writes `require` into __main__ globals; harmless
    client = RemoteAPIClient(host, port, verbose=0)
    # hazard: the client has no timeout API and blocks forever in recv without these
    client.socket.setsockopt(zmq.RCVTIMEO, int(_timeout_s() * MS_PER_S))
    client.socket.setsockopt(zmq.SNDTIMEO, int(_timeout_s() * MS_PER_S))
    client.socket.setsockopt(zmq.LINGER, 0)
    return client


def _reset() -> None:
    """Discard the connection; a REQ socket is unusable after a missed reply (CALL-10)."""
    global _client
    client, _client = _client, None
    if client is not None:
        client.socket.close()
        client.context.term()


def _invoke(entry: dict[str, Any], positional: list[Any]) -> Any:
    global _client
    if _client is None:
        _client = _new_client()
    namespace = _client.require(entry["namespace"])
    try:
        member = getattr(namespace, entry["method"])
    except AttributeError:
        raise catalog.VrepError(
            f"CoppeliaSim error in {entry['name']}: "
            "function not available in the connected CoppeliaSim"
        ) from None
    return member if entry["kind"] == "constant" else member(*positional)


def call(name: str, arguments: dict[str, Any] | None = None) -> Any:
    entry = catalog.get(name)
    # invariant: validate before any network I/O (CALL-04..07); constants ignore arguments
    positional = (
        []
        if entry["kind"] == "constant"
        else catalog.to_positional(name, arguments or {})
    )
    with _lock:
        try:
            return jsonable(_invoke(entry, positional))
        except zmq.Again:
            _reset()
            host, port = _host_port()
            raise catalog.VrepError(
                f"CoppeliaSim not reachable at {host}:{port} (timeout {_timeout_s():g}s). "
                "Start CoppeliaSim with the ZMQ remote API add-on and retry."
            ) from None
        except catalog.VrepError:
            raise
        except Exception as exc:
            raise catalog.VrepError(f"CoppeliaSim error in {name}: {exc}") from exc
