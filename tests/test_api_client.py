import json

import pytest
import requests

from agentlab.api_client import ApiClient


class DummyResponse:
    def __init__(self, status_code=200, payload=None, text="{}") -> None:
        self._payload = payload
        self.status_code = status_code
        self.text = text

    def raise_for_status(self):
        if self.status_code >= 400:
            raise Exception("HTTP error")  # Simplified

    def json(self):
        if self._payload is not None:
            return self._payload
        return json.loads(self.text)


def test_get_json_parses_ok(monkeypatch):
    def fake_get(url, params=None, timeout=5.0):
        return DummyResponse(200, payload={"ok": True})

    monkeypatch.setattr(requests, "get", fake_get)
    client = ApiClient("https://example.com")
    assert client.get_json("/ping") == {"ok": True}


def test_get_json_retries_on_connection_error(monkeypatch):
    """Test that connection errors trigger retries."""
    call_count = 0

    def fake_get(url, params=None, timeout=5.0):
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            raise requests.exceptions.ConnectionError("Connection failed")
        return DummyResponse(200, payload={"success": True})

    monkeypatch.setattr(requests, "get", fake_get)
    client = ApiClient("https://example.com", max_retries=3, backoff_factor=0.01)
    result = client.get_json("/data")

    assert result == {"success": True}
    assert call_count == 3  # Failed twice, succeeded on third attempt


def test_get_json_retries_on_timeout(monkeypatch):
    """Test that timeout errors trigger retries."""
    call_count = 0

    def fake_get(url, params=None, timeout=5.0):
        nonlocal call_count
        call_count += 1
        if call_count < 2:
            raise requests.exceptions.Timeout("Request timed out")
        return DummyResponse(200, payload={"data": "value"})

    monkeypatch.setattr(requests, "get", fake_get)
    client = ApiClient("https://example.com", max_retries=3, backoff_factor=0.01)
    result = client.get_json("/endpoint")

    assert result == {"data": "value"}
    assert call_count == 2  # Failed once, succeeded on second attempt


def test_get_json_exhausts_all_retries(monkeypatch):
    """Test that after exhausting all retries, the exception is raised."""
    call_count = 0

    def fake_get(url, params=None, timeout=5.0):
        nonlocal call_count
        call_count += 1
        raise requests.exceptions.ConnectionError("Persistent connection error")

    monkeypatch.setattr(requests, "get", fake_get)
    client = ApiClient("https://example.com", max_retries=3, backoff_factor=0.01)

    with pytest.raises(requests.exceptions.ConnectionError):
        client.get_json("/failing")

    assert call_count == 4  # Initial attempt + 3 retries


def test_get_json_http_error_no_retry(monkeypatch):
    """Test that HTTP errors (4xx, 5xx) do not trigger retries."""
    call_count = 0

    def fake_get(url, params=None, timeout=5.0):
        nonlocal call_count
        call_count += 1
        response = DummyResponse(404)
        return response

    monkeypatch.setattr(requests, "get", fake_get)
    client = ApiClient("https://example.com", max_retries=3, backoff_factor=0.01)

    # HTTP errors should raise immediately without retrying
    with pytest.raises(Exception):  # DummyResponse raises generic Exception
        client.get_json("/notfound")

    assert call_count == 1  # No retries for HTTP errors


def test_get_json_custom_timeout(monkeypatch):
    """Test that custom timeout is passed to requests."""
    captured_timeout = None

    def fake_get(url, params=None, timeout=5.0):
        nonlocal captured_timeout
        captured_timeout = timeout
        return DummyResponse(200, payload={"result": "ok"})

    monkeypatch.setattr(requests, "get", fake_get)
    client = ApiClient("https://example.com", timeout=10.0)
    client.get_json("/test")

    assert captured_timeout == 10.0


def test_get_json_with_params(monkeypatch):
    """Test that query parameters are passed correctly."""
    captured_params = None

    def fake_get(url, params=None, timeout=5.0):
        nonlocal captured_params
        captured_params = params
        return DummyResponse(200, payload={"result": "ok"})

    monkeypatch.setattr(requests, "get", fake_get)
    client = ApiClient("https://example.com")
    client.get_json("/search", params={"q": "test", "limit": 10})

    assert captured_params == {"q": "test", "limit": 10}


def test_get_json_invalid_json_returns_empty_dict(monkeypatch):
    """Test that invalid JSON returns an empty dict."""

    def fake_get(url, params=None, timeout=5.0):
        response = DummyResponse(200, text="invalid json{")
        return response

    monkeypatch.setattr(requests, "get", fake_get)
    client = ApiClient("https://example.com")
    result = client.get_json("/bad-json")

    assert result == {}
