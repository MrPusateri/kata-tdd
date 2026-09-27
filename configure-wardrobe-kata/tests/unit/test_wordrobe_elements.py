from configure_wardrobe_kata.domain.currencies import Currencies
from configure_wardrobe_kata.domain.wardrobe_element import WardrobeElement

def test_small_wardrobe_element_is_50cm_and_price_59_usd(swedish_furniture_catalog):
    we: WardrobeElement = swedish_furniture_catalog["SMALL-WE"]

    assert we.length == 50
    assert we.price == 59
    assert we.currency == Currencies.USD

def test_medium_wardrobe_element_is_75cm_and_price_62_usd(swedish_furniture_catalog):
    we: WardrobeElement = swedish_furniture_catalog["MEDIUM-WE"]

    assert we.length == 75
    assert we.price == 62
    assert we.currency == Currencies.USD

def test_large_wardrobe_element_is_100cm_and_price_90_usd(swedish_furniture_catalog):
    we: WardrobeElement = swedish_furniture_catalog["LARGE-WE"]

    assert we.length == 100
    assert we.price == 90
    assert we.currency == Currencies.USD

def test_extra_large_wardrobe_element_is_120cm_and_price_111_usd(swedish_furniture_catalog):
    we: WardrobeElement = swedish_furniture_catalog["EXTRA-LARGE-WE"]

    assert we.length == 120
    assert we.price == 111
    assert we.currency == Currencies.USD
