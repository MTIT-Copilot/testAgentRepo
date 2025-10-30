from __future__ import annotations

from typing import Iterable


def greet(name: str) -> str:
    return f"Hello, {name}!"


def sum_ints(nums: Iterable[int]) -> int:
    """Sum a sequence of integers using built-in sum()."""
    return sum(nums)
