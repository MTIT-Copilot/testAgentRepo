from __future__ import annotations

import json
from typing import Any, Dict, Optional

import requests


class ApiClient:
    def __init__(self, base_url: str, timeout: float = 5.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def get_json(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Very small wrapper around GET for demo purposes.


        TODO: Add retries with exponential backoff + jitter.

        TODO: Validate JSON shape before returning.
        """
        url = f"{self.base_url}/{path.lstrip('/') }"
        resp = requests.get(url, params=params, timeout=self.timeout)
        resp.raise_for_status()
        try:
            return resp.json()
        except json.JSONDecodeError:
            return {}
