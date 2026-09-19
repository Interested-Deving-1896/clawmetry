from __future__ import annotations
import sys
import os
from pathlib import Path


def _post_json(url, body, timeout=15):
    """POST JSON and return (result_dict, status).

    On 2xx: returns (parsed_json, 200).
    On HTTPError: returns ({"error": msg, "retry_after": int|None}, status_code).
    On other errors: returns ({"error": str(e)}, 0).
    """
    import urllib.request
    import urllib.error
    import json as _json

    data = _json.dumps(body).encode()
    req = urllib.request.Request(
        url, data=data, headers={"Content-Type": "application/json"}, method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return _json.loads(resp.read()), 200
    except urllib.error.HTTPError as e:
        raw = e.read().decode()
        try:
            payload = _json.loads(raw)
        except Exception:
            payload = {}
        return (
            {
                "error": payload.get("error") or raw[:200],
                "retry_after": payload.get("retry_after"),
            },
            e.code,
        )
    except Exception as e:
        return {"error": str(e)}, 0
