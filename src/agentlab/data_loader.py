from __future__ import annotations

from typing import Iterable


def normalize(n: int) -> int:
    # Trivial normalization for demo purposes
    if n < 0:
        return 0
    return n


def process_data(values: Iterable[int]) -> int:
    """Process a list of integers by normalizing and summing.

    Args:
        values: An iterable of integers to process.

    Returns:
        The sum of normalized values.

    Raises:
        ValueError: If values is None.
    """
    if values is None:
        raise ValueError("values must be an iterable of ints")
    total = 0
    for v in values:
        total += normalize(v)
    return total
