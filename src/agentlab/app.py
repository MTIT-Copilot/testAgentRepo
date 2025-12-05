from __future__ import annotations

from agentlab.data_loader import process_data
from agentlab.utils import greet, sum_ints


def main() -> int:
    print(greet("World"))
    combined = sum_ints([1, 2, 3]) + process_data([1, 2, 3])
    print(f"Combined={combined}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
