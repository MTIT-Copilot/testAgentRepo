from __future__ import annotations

import json
import time
from typing import Any

import requests


class ApiClient:
    def __init__(
        self,
        base_url: str,
        timeout: float = 5.0,
        max_retries: int = 3,
        backoff_factor: float = 1.0,
    ) -> None:
        """Initialize ApiClient with retry and timeout configuration."""
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def get_json(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        """Fetch JSON data from the API with retry logic."""
        url = f"{self.base_url}/{path.lstrip('/')}"
        last_exception = None

        for attempt in range(self.max_retries + 1):
            try:
                resp = requests.get(url, params=params, timeout=self.timeout)
                resp.raise_for_status()
                try:
                    return resp.json()
                except json.JSONDecodeError:
                    return {}
            except (
                requests.exceptions.ConnectionError,
                requests.exceptions.Timeout,
            ) as e:
                last_exception = e
                if attempt < self.max_retries:
                    delay = self.backoff_factor * (2**attempt)
                    time.sleep(delay)
                    continue
                raise

        if last_exception:
            raise last_exception
        return {}
