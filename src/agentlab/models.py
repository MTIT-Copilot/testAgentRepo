from __future__ import annotations

from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str

    def display(self) -> str:
        # TODO: Add formatting options, e.g., uppercase flag
        return f"User({self.id}, {self.name})"
