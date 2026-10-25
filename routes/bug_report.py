"""Local support relay. Only a user's explicit submission leaves the machine."""
import json
import logging
import urllib.error
import urllib.request
from urllib.parse import urlsplit

from flask import Blueprint, jsonify, request
from clawmetry.bug_report import MAX_BODY_BYTES, validate_report

bp_bug_report = Blueprint("bug_report", __name__)
log = logging.getLogger(__name__)
SUPPORT_URL = "https://app.clawmetry.com/api/support/bugs"


@bp_bug_report.route("/api/support/bugs", methods=["POST"])
def submit_bug_report():
    origin = request.headers.get("Origin")
    if origin and urlsplit(origin).netloc != request.host:
        return jsonify(error="Please send the report from your ClawMetry dashboard."), 403
    if request.content_length and request.content_length > MAX_BODY_BYTES:
        return jsonify(error="Please choose a screenshot smaller than 4 MB."), 413
    raw = request.stream.read(MAX_BODY_BYTES + 1)
    if len(raw) > MAX_BODY_BYTES:
        return jsonify(error="Please choose a screenshot smaller than 4 MB."), 413
    try:
        report = validate_report(json.loads(raw))
    except (ValueError, UnicodeError) as exc:
        message = str(exc) if not isinstance(exc, (json.JSONDecodeError, UnicodeError)) else "Please reopen the report form and try again."
        return jsonify(error=message), 400
    try:
        relay = urllib.request.Request(SUPPORT_URL, data=json.dumps(report).encode(),
                                       headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(relay, timeout=25) as response:
            result = json.load(response)
        if result.get("ok") is True and result.get("id") == report["id"]:
            return jsonify(ok=True, id=report["id"])
    except urllib.error.HTTPError as exc:
        if exc.code == 429:
            return jsonify(error="You have sent several reports. Please wait a few minutes and try again."), 429
        log.warning("Bug report delivery returned HTTP %s", exc.code)
    except Exception as exc:
        log.warning("Bug report delivery failed: %s", type(exc).__name__)
    return jsonify(error="Your report could not be sent. Your draft is still here. Please try again, or email vivek@clawmetry.com."), 502
