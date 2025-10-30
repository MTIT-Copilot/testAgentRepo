from __future__ import annotations

import json
import time
from typing import Any, Dict, Optional

import requests


class ApiClient:
    def __init__(
        self, base_url: str, timeout: float = 5.0, max_retries: int = 3, backoff_factor: float = 1.0
    ) -> None:
        """Initialize ApiClient with retry and timeout configuration.

        Args:
            base_url: Base URL for API requests
            timeout: Request timeout in seconds (default: 5.0)
            max_retries: Maximum number of retry attempts (default: 3)
            backoff_factor: Exponential backoff multiplier (default: 1.0)
                           Delay = backoff_factor * (2 ** retry_attempt)
        """
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def get_json(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Fetch JSON data from the API with retry logic.

        Retries up to max_retries times on connection errors with exponential backoff.
        The delay between retries follows: backoff_factor * (2 ** retry_attempt) seconds.

        Args:
            path: API endpoint path
            params: Optional query parameters

        Returns:
            Dictionary containing JSON response data

        Raises:
            requests.exceptions.RequestException: After exhausting all retries
            requests.exceptions.HTTPError: For HTTP error status codes

        Examples:
            - Retry 0 (first attempt): No delay
            - Retry 1: backoff_factor * 2^0 = 1.0 seconds (default)
            - Retry 2: backoff_factor * 2^1 = 2.0 seconds (default)
            - Retry 3: backoff_factor * 2^2 = 4.0 seconds (default)
        """
        url = f"{self.base_url}/{path.lstrip('/') }"
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
                    # Calculate exponential backoff delay
                    delay = self.backoff_factor * (2**attempt)
                    time.sleep(delay)
                    continue
                # If we've exhausted all retries, raise the last exception
                raise

        # This should never be reached, but just in case
        if last_exception:
            raise last_exception
        return {}
