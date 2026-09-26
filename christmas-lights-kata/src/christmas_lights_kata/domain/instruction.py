from dataclasses import dataclass
from enum import Enum, auto

from christmas_lights_kata.domain.rectangle import Rectangle


class Operation(Enum):
    TURN_ON = auto()
    TURN_OFF = auto()
    TOGGLE = auto()


@dataclass(frozen=True)
class Instruction:
    """One of Santa's instructions: an operation to apply to a rectangle of lights."""

    operation: Operation
    rectangle: Rectangle
