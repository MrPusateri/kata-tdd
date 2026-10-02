from typing import Set

from configure_wardrobe_kata.domain.wardrobe_element import WardrobeElement
from configure_wardrobe_kata.domain.combinations import combine, cheap_combinations
from configure_wardrobe_kata.domain.currencies import Currencies

def test_single_combination_fills_a_50cm_wall_exactly(swedish_furniture_catalog: Set[WardrobeElement]):
    combinations = combine(catalog=swedish_furniture_catalog, wall_length=50)

    assert len(combinations) == 1

def test_returns_empty_list_when_no_combination_fills_the_wall_exactly(swedish_furniture_catalog: Set[WardrobeElement]):
    combinations = combine(catalog=swedish_furniture_catalog, wall_length=25)

    assert combinations == []

def test_returns_multiple_combinations_for_a_250cm_wall(swedish_furniture_catalog: Set[WardrobeElement]):
    combinations = combine(catalog=swedish_furniture_catalog, wall_length=250)

    # uv run pytest -s tests/unit/test_combinations.py
    print(combinations)

    assert len(combinations) > 1

def test_cheapest_combination_has_the_lowest_total_price(swedish_furniture_catalog: Set[WardrobeElement]):
    combinations = cheap_combinations(swedish_furniture_catalog, 100)

    assert len(combinations) == 2
    assert combinations[0] == [we for we in swedish_furniture_catalog if we.we_id == "LARGE-WE"]

def test_cheapest_combination_among_ties_returns_one_valid_option():
    custom_catalog = set(
        [
            WardrobeElement("EXTRA-SMALL-WE", 40, 30, Currencies.USD),
            WardrobeElement("SMALL-WE", 50, 59, Currencies.USD),
            WardrobeElement("SMALL-MEDIUM-WE", 60, 60, Currencies.USD),
            WardrobeElement("LARGE-WE", 100, 90, Currencies.USD)
        ]
    )

    combinations = cheap_combinations(custom_catalog, 100)

    assert len(combinations) == 3
    assert combinations[0] == [we for we in custom_catalog if we.we_id == "LARGE-WE"]
