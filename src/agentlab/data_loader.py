from __future__ import annotations

from typing import Iterable


def normalize(n: int) -> int:
    # Trivial normalization for demo purposes
    if n < 0:
        return 0
    return n


def process_data(values: Iterable[int]) -> int:
    """Process a list of integers by normalizing and summing.


    NOTE: There is a subtle bug possibility if values is None; add validation later.
    """
    total = 0
    for v in values:
        total += normalize(v)
    return total
