"""Support must send only explicit fields, reject bad uploads, and fail honestly."""
import base64
import io
import json
from pathlib import Path
import uuid
from unittest.mock import patch

import pytest
from flask import Flask
from clawmetry.bug_report import MAX_IMAGE_BYTES, validate_report
from routes.bug_report import bp_bug_report


def report(**fields):
    return dict({'id': str(uuid.uuid4()), 'description': 'The cost chart is blank.',
                 'categories': ['data'], 'details': {}, 'email': ''}, **fields)


def test_only_explicit_details_are_forwarded():
    clean = validate_report(report(details={'version': '1.2', 'token': 'secret', 'url': '?token=secret'}, logs='private'))
    assert clean['details'] == {'version': '1.2'}
    assert 'logs' not in clean


@pytest.mark.parametrize('fields', [
    {'description': 'short'}, {'description': []}, {'email': 'a@b.com\r\nBcc:x@y.com'},
    {'categories': ['unknown']}, {'categories': [{}]}, {'details': []}, {'id': 15},
    {'screenshot': {'content': base64.b64encode(b'<svg onload="alert(1)">').decode()}},
    {'screenshot': {'content': 'not base64'}}, {'screenshot': {'content': 'a' * (MAX_IMAGE_BYTES * 2)}},
])
def test_bad_input_is_rejected(fields):
    with pytest.raises(ValueError):
        validate_report(report(**fields))


def test_screenshot_name_is_derived_from_bytes():
    content = base64.b64encode(b'\x89PNG\r\n\x1a\nimage').decode()
    clean = validate_report(report(screenshot={'filename': '../../private.svg', 'content': content}))
    assert clean['screenshot'] == {'filename': 'screenshot.png', 'content': content}


@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(bp_bug_report)
    return app.test_client()


def test_relay_confirms_only_a_matching_receipt(client):
    data = report()
    with patch('routes.bug_report.urllib.request.urlopen') as post:
        post.return_value.__enter__.return_value = io.BytesIO(json.dumps({'ok': True, 'id': data['id']}).encode())
        assert client.post('/api/support/bugs', json=data).json == {'ok': True, 'id': data['id']}
        outgoing = json.loads(post.call_args.args[0].data)
        assert outgoing['description'] == data['description']
        post.return_value.__enter__.return_value = io.BytesIO(b'{"ok":true,"id":"wrong"}')
        assert client.post('/api/support/bugs', json=data).status_code == 502


def test_relay_failure_and_cross_origin_are_honest(client):
    with patch('routes.bug_report.urllib.request.urlopen', side_effect=TimeoutError):
        res = client.post('/api/support/bugs', json=report())
        assert res.status_code == 502 and 'draft' in res.json['error']
        res = client.post('/api/support/bugs', json=report(), headers={'Origin': 'https://elsewhere.example'})
        assert res.status_code == 403


def test_malformed_json_never_crashes(client):
    assert client.post('/api/support/bugs', data=b'{oops').status_code == 400


def test_live_template_loads_the_report_form():
    root = Path(__file__).resolve().parents[1]
    assert "{% include 'partials/bug-report.html' %}" in (root / 'dashboard.py').read_text()
    template = (root / 'clawmetry/templates/partials/bug-report.html').read_text()
    assert 'bug-report-dialog' in template and 'js/bug-report.js' in template
