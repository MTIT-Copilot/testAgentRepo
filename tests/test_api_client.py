import json

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

    import requests
    monkeypatch.setattr(requests, "get", fake_get)
    client = ApiClient("https://example.com")
    assert client.get_json("/ping") == {"ok": True}
