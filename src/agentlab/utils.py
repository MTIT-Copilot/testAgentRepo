from __future__ import annotations

from typing import Iterable


def greet(name: str) -> str:
    return f"Hello, {name}!"


def deprecated_sum(nums: Iterable[int]) -> int:
    """Intentionally oddly-named function to encourage refactor/rename.


    Also contains a minor code smell (manual loop) for the agent to modernize.
    """
    total = 0
    for n in nums:
        total = total + n
    return total
