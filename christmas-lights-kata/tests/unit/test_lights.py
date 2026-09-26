import re

import pytest

from christmas_lights_kata.domain.exceptions.light_does_not_exist import LightDoesNotExist
from christmas_lights_kata.domain.grid import Grid
from christmas_lights_kata.domain.instruction import Instruction, Operation
from christmas_lights_kata.domain.rectangle import Rectangle


def light(x: int, y: int) -> Rectangle:
    return Rectangle((x, y), (x, y))


def test_new_grid_has_no_lights_on():
    grid = Grid(x_dimension=3, y_dimension=3)

    assert grid.n_lights_on == 0


def test_turn_on_a_single_light_turns_on_one_light():
    grid = Grid(x_dimension=3, y_dimension=3)

    grid.turn_on(light(0, 1))

    assert grid.is_on(0, 1)
    assert grid.n_lights_on == 1


def test_turn_on_an_already_on_light_leaves_it_on():
    grid = Grid(x_dimension=3, y_dimension=3)

    grid.turn_on(light(0, 1))
    grid.turn_on(light(0, 1))

    assert grid.is_on(0, 1)
    assert grid.n_lights_on == 1


def test_turn_on_a_range_turns_on_every_light_inside_it():
    grid = Grid(x_dimension=3, y_dimension=3)

    grid.turn_on(Rectangle((1, 1), (2, 2)))

    assert grid.is_on(1, 1)
    assert grid.is_on(1, 2)
    assert grid.is_on(2, 1)
    assert grid.is_on(2, 2)
    assert grid.n_lights_on == 4


def test_turn_on_a_range_leaves_lights_outside_it_off():
    grid = Grid(x_dimension=3, y_dimension=3)

    grid.turn_on(Rectangle((1, 0), (2, 2)))

    assert not grid.is_on(0, 0)
    assert not grid.is_on(0, 1)
    assert not grid.is_on(0, 2)


def test_cannot_turn_on_a_light_that_does_not_exist():
    grid = Grid(x_dimension=3, y_dimension=3)

    with pytest.raises(LightDoesNotExist, match=re.escape("(4,4)")):
        grid.turn_on(light(4, 4))


def test_lights_exist_up_to_the_last_index_of_each_dimension():
    grid = Grid(x_dimension=4, y_dimension=2)

    grid.turn_on(light(3, 1))

    assert grid.is_on(3, 1)
    with pytest.raises(LightDoesNotExist):
        grid.turn_on(light(4, 0))
    with pytest.raises(LightDoesNotExist):
        grid.turn_on(light(0, 2))


def test_turn_on_a_range_partially_outside_the_grid_turns_on_nothing():
    grid = Grid(x_dimension=3, y_dimension=3)

    with pytest.raises(LightDoesNotExist):
        grid.turn_on(Rectangle((1, 1), (5, 5)))

    assert grid.n_lights_on == 0


def test_turn_off_a_light_that_is_on_turns_it_off():
    grid = Grid(x_dimension=3, y_dimension=3)
    grid.turn_on(light(0, 1))

    grid.turn_off(light(0, 1))

    assert not grid.is_on(0, 1)
    assert grid.n_lights_on == 0


def test_turn_off_an_already_off_light_leaves_it_off():
    grid = Grid(x_dimension=3, y_dimension=3)

    grid.turn_off(light(0, 1))

    assert not grid.is_on(0, 1)


def test_turn_off_a_range_partially_outside_the_grid_turns_off_nothing():
    grid = Grid(x_dimension=3, y_dimension=3)
    grid.turn_on(Rectangle((0, 0), (2, 2)))

    with pytest.raises(LightDoesNotExist):
        grid.turn_off(Rectangle((1, 1), (5, 5)))

    assert grid.n_lights_on == 9


def test_toggle_a_rectangle_with_one_light_on_will_turns_it_off_and_turns_on_others():
    grid = Grid(x_dimension=3, y_dimension=3)

    grid.turn_on(light(1,1))

    grid.toggle(Rectangle((0,0), (2,1)))

    assert grid.n_lights_on == 5
    assert not grid.is_on(1,1)


def test_toggle_a_rectangle_does_not_alterate_lights_outside_the_rectangle():
    grid = Grid(x_dimension=3, y_dimension=3)

    grid.turn_on(light(1,1))

    grid.toggle(Rectangle((0,0), (2,1)))

    assert not grid.is_on(0,2)
    assert not grid.is_on(1,2)
    assert not grid.is_on(2,2)


def test_cannot_toggle_a_light_that_does_not_exist():
    grid = Grid(x_dimension=3, y_dimension=3)

    with pytest.raises(LightDoesNotExist, match=re.escape("(4,4)")):
        grid.toggle(light(4, 4))


def test_toggle_a_range_partially_outside_the_grid_toggles_nothing():
    grid = Grid(x_dimension=3, y_dimension=3)
    grid.turn_on(Rectangle((0, 0), (2, 2)))

    with pytest.raises(LightDoesNotExist):
        grid.toggle(Rectangle((1, 1), (5, 5)))

    assert grid.n_lights_on == 9


def test_toggling_a_rectangle_twice_restores_its_original_state():
    grid = Grid(x_dimension=3, y_dimension=3)
    grid.turn_on(light(1, 1))
    rectangle = Rectangle((0, 0), (2, 1))

    grid.toggle(rectangle)
    grid.toggle(rectangle)

    assert grid.is_on(1, 1)
    assert grid.n_lights_on == 1


def test_instructions_are_applied_in_order():
    grid = Grid(x_dimension=3, y_dimension=3)
    rectangle = Rectangle((0, 0), (2, 2))

    grid.apply_all([
        Instruction(Operation.TURN_ON, rectangle),
        Instruction(Operation.TOGGLE, rectangle),
    ])

    assert grid.n_lights_on == 0


def test_santas_instructions_light_up_the_expected_number_of_lights():
    grid = Grid(x_dimension=1000, y_dimension=1000)

    grid.apply_all([
        Instruction(Operation.TURN_ON, Rectangle((887, 9), (959, 629))),
        Instruction(Operation.TURN_ON, Rectangle((454, 398), (844, 448))),
        Instruction(Operation.TURN_OFF, Rectangle((539, 243), (559, 965))),
        Instruction(Operation.TURN_OFF, Rectangle((370, 819), (676, 868))),
        Instruction(Operation.TURN_OFF, Rectangle((145, 40), (370, 997))),
        Instruction(Operation.TURN_OFF, Rectangle((301, 3), (808, 453))),
        Instruction(Operation.TURN_ON, Rectangle((351, 678), (951, 908))),
        Instruction(Operation.TOGGLE, Rectangle((720, 196), (897, 994))),
        Instruction(Operation.TOGGLE, Rectangle((831, 394), (904, 860))),
    ])

    assert grid.n_lights_on == 230022
