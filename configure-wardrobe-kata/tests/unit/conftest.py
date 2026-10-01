import pytest

from configure_wardrobe_kata.domain.wardrobe_element import WardrobeElement
from configure_wardrobe_kata.domain.currencies import Currencies

@pytest.fixture
def swedish_furniture_catalog():
    return set(
        [WardrobeElement("SMALL-WE", 50, 59, Currencies.USD),
        WardrobeElement("MEDIUM-WE", 75, 62, Currencies.USD),
        WardrobeElement("LARGE-WE", 100, 90, Currencies.USD),
        WardrobeElement("EXTRA-LARGE-WE", 120, 111, Currencies.USD)]
    )