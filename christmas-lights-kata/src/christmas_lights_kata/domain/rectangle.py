from collections.abc import Iterator
from dataclasses import dataclass


@dataclass(frozen=True, init=False)
class Rectangle:
    """Inclusive rectangle of lights, given by two opposite corners in any order."""

    x_min: int
    y_min: int
    x_max: int
    y_max: int

    def __init__(self, first_corner: tuple[int, int], second_corner: tuple[int, int]):
        object.__setattr__(self, "x_min", min(first_corner[0], second_corner[0]))
        object.__setattr__(self, "y_min", min(first_corner[1], second_corner[1]))
        object.__setattr__(self, "x_max", max(first_corner[0], second_corner[0]))
        object.__setattr__(self, "y_max", max(first_corner[1], second_corner[1]))

    def coordinates(self) -> Iterator[tuple[int, int]]:
        for x in range(self.x_min, self.x_max + 1):
            for y in range(self.y_min, self.y_max + 1):
                yield (x, y)
