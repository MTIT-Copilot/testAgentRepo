from __future__ import annotations

from agentlab.api_client import ApiClient
from agentlab.data_loader import process_data
from agentlab.utils import greet, sum_ints


def main() -> int:
    # TODO: Add proper logging (INFO level, include timestamp)
    print(greet("World"))  # intentionally uses print (to refactor to logging)
    ApiClient(base_url="https://example.com")
    # NOTE: ApiClient.get_json currently lacks retries/backoff. See SCENARIOS.
    combined = sum_ints([1, 2, 3]) + process_data([1, 2, 3])
    print(f"Combined={combined}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
