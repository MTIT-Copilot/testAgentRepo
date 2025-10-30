from __future__ import annotations

from agentlab.utils import greet, deprecated_sum
from agentlab.data_loader import process_data
from agentlab.api_client import ApiClient


def main() -> int:
    # TODO: Add proper logging (INFO level, include timestamp)
    print(greet("World"))  # intentionally uses print (to refactor to logging)
    client = ApiClient(base_url="https://example.com")
    # NOTE: ApiClient.get_json currently lacks retries/backoff. See SCENARIOS.
    combined = deprecated_sum([1, 2, 3]) + process_data([1, 2, 3])
    # NOTE: 'deprecated_sum' is intentionally named to trigger a refactor scenario.
    print(f"Combined={combined}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
