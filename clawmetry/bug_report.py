"""Bounded, explicit support submissions. Never collect logs or credentials."""
import base64
import binascii
import re
import uuid

MAX_IMAGE_BYTES = 4 * 1024 * 1024
MAX_BODY_BYTES = 6 * 1024 * 1024
CATEGORIES = {"display", "data", "broken"}


def validate_report(data):
    """Return only the fields support needs; reject malformed attachments."""
    if not isinstance(data, dict):
        raise ValueError("Please describe the issue and try again.")
    description = data.get("description", "")
    if not isinstance(description, str) or not 10 <= len(description.strip()) <= 10000:
        raise ValueError("Please describe the issue in 10 to 10,000 characters.")
    email = data.get("email", "")
    if not isinstance(email, str) or len(email) > 254 or (email and not re.fullmatch(r"[^\s@<>]+@[^\s@<>]+\.[^\s@<>]+", email)):
        raise ValueError("Please enter a valid reply email, or leave it empty.")
    try:
        report_id = str(uuid.UUID(data.get("id", "")))
    except (ValueError, TypeError, AttributeError):
        raise ValueError("Please reopen the report form and try again.")
    categories = data.get("categories", [])
    if not isinstance(categories, list) or len(categories) > 3 or any(not isinstance(c, str) or c not in CATEGORIES for c in categories):
        raise ValueError("Please choose the issue types again.")
    details = data.get("details", {})
    if not isinstance(details, dict):
        raise ValueError("Please reopen the report form and try again.")
    # Never accept a URL, node ID, query string, logs, or arbitrary metadata.
    safe_details = {}
    for key in ("version", "view", "runtime", "browser", "hosting"):
        value = details.get(key, "")
        if not isinstance(value, str) or len(value) > 300:
            raise ValueError("Please reopen the report form and try again.")
        if value:
            safe_details[key] = value
    result = {"id": report_id, "description": description.strip(), "email": email,
              "categories": sorted(set(categories)), "details": safe_details}
    screenshot = data.get("screenshot")
    if screenshot is not None:
        if not isinstance(screenshot, dict):
            raise ValueError("Please attach a PNG, JPEG, or WebP screenshot.")
        content = screenshot.get("content", "")
        if not isinstance(content, str) or len(content) > 4 * ((MAX_IMAGE_BYTES + 2) // 3):
            raise ValueError("Please choose a screenshot smaller than 4 MB.")
        try:
            raw = base64.b64decode(content, validate=True)
        except (ValueError, binascii.Error):
            raise ValueError("Please attach a PNG, JPEG, or WebP screenshot.")
        if not raw or len(raw) > MAX_IMAGE_BYTES:
            raise ValueError("Please choose a screenshot smaller than 4 MB.")
        if raw.startswith(b"\x89PNG\r\n\x1a\n"):
            extension = "png"
        elif raw.startswith(b"\xff\xd8\xff"):
            extension = "jpg"
        elif raw.startswith(b"RIFF") and raw[8:12] == b"WEBP":
            extension = "webp"
        else:
            raise ValueError("Please attach a PNG, JPEG, or WebP screenshot.")
        result["screenshot"] = {"filename": "screenshot." + extension, "content": content}
    return result
