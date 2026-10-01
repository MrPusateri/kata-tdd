from typing import Set

from configure_wardrobe_kata.domain.currencies import Currencies
from configure_wardrobe_kata.domain.wardrobe_element import WardrobeElement

def test_small_wardrobe_element_is_50cm_and_price_59_usd(swedish_furniture_catalog: Set[WardrobeElement]):
    we = [we for we in swedish_furniture_catalog if we.we_id == "SMALL-WE"][0]

    assert we.length == 50
    assert we.price == 59
    assert we.currency == Currencies.USD

def test_medium_wardrobe_element_is_75cm_and_price_62_usd(swedish_furniture_catalog: Set[WardrobeElement]):
    we = [we for we in swedish_furniture_catalog if we.we_id == "MEDIUM-WE"][0]

    assert we.length == 75
    assert we.price == 62
    assert we.currency == Currencies.USD

def test_large_wardrobe_element_is_100cm_and_price_90_usd(swedish_furniture_catalog: Set[WardrobeElement]):
    we = [we for we in swedish_furniture_catalog if we.we_id == "LARGE-WE"][0]

    assert we.length == 100
    assert we.price == 90
    assert we.currency == Currencies.USD

def test_extra_large_wardrobe_element_is_120cm_and_price_111_usd(swedish_furniture_catalog: Set[WardrobeElement]):
    we = [we for we in swedish_furniture_catalog if we.we_id == "EXTRA-LARGE-WE"][0]

    assert we.length == 120
    assert we.price == 111
    assert we.currency == Currencies.USD

def test_sort_wardrobe_element_small_and_large(swedish_furniture_catalog: Set[WardrobeElement]):
    small_we = [we for we in swedish_furniture_catalog if we.we_id == "SMALL-WE"][0]
    large_we = [we for we in swedish_furniture_catalog if we.we_id == "LARGE-WE"][0]

    assert small_we < large_we
    assert sorted([large_we, small_we])[0] == small_we

