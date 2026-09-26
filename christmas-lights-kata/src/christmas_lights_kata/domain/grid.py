from collections.abc import Iterable

from christmas_lights_kata.domain.exceptions.light_does_not_exist import LightDoesNotExist
from christmas_lights_kata.domain.instruction import Instruction, Operation
from christmas_lights_kata.domain.rectangle import Rectangle

_OPERATIONS = {
    Operation.TURN_ON: lambda grid, rectangle: grid.turn_on(rectangle),
    Operation.TURN_OFF: lambda grid, rectangle: grid.turn_off(rectangle),
    Operation.TOGGLE: lambda grid, rectangle: grid.toggle(rectangle),
}


class Grid:

    def __init__(self, x_dimension: int, y_dimension: int):
        self._lights = {(x, y): False for x in range(x_dimension) for y in range(y_dimension)}

    @property
    def n_lights_on(self) -> int:
        return sum(self._lights.values())

    def is_on(self, x: int, y: int) -> bool:
        self._ensure_exists(x, y)
        return self._lights[(x, y)]

    def turn_on(self, rectangle: Rectangle) -> None:
        self._switch(rectangle, on=True)

    def turn_off(self, rectangle: Rectangle) -> None:
        self._switch(rectangle, on=False)

    def toggle(self, rectangle: Rectangle) -> None:
        self._ensure_rectangle_exists(rectangle)

        for coordinates in rectangle.coordinates():
            self._lights[coordinates] = not self._lights[coordinates]

    def apply(self, instruction: Instruction) -> None:
        _OPERATIONS[instruction.operation](self, instruction.rectangle)

    def apply_all(self, instructions: Iterable[Instruction]) -> None:
        for instruction in instructions:
            self.apply(instruction)

    def _switch(self, rectangle: Rectangle, on: bool) -> None:
        # The grid is a full rectangle, so if the two opposite corners of the
        # range exist, every light between them exists: validate before mutating.
        self._ensure_rectangle_exists(rectangle)

        for coordinates in rectangle.coordinates():
            self._lights[coordinates] = on

    def _ensure_exists(self, x: int, y: int) -> None:
        if (x, y) not in self._lights:
            raise LightDoesNotExist(f"The light ({x},{y}) does not exist.")

    def _ensure_rectangle_exists(self, rectangle: Rectangle) -> None:
        self._ensure_exists(rectangle.x_min, rectangle.y_min)
        self._ensure_exists(rectangle.x_max, rectangle.y_max)
