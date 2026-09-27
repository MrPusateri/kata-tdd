import pytest

from configure_wardrobe_kata.domain.wardrobe_element import WardrobeElement
from configure_wardrobe_kata.domain.currencies import Currencies

@pytest.fixture
def swedish_furniture_catalog():
    return {
        "SMALL-WE": WardrobeElement(50, 59, Currencies.USD),
        "MEDIUM-WE": WardrobeElement(75, 62, Currencies.USD),
        "LARGE-WE": WardrobeElement(100, 90, Currencies.USD),
        "EXTRA-LARGE-WE": WardrobeElement(120, 111, Currencies.USD)
    }