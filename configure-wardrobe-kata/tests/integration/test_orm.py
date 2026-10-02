from sqlalchemy import text

from configure_wardrobe_kata.domain.wardrobe_element import WardrobeElement
from configure_wardrobe_kata.domain.currencies import Currencies


def test_orderline_mapper_can_load_lines(session):
    session.execute(
        text(
            "INSERT INTO wardrobe_catalog (we_id, length, price, currency) VALUES "
            '("SMALL-WE", 50, 59, "USD"),'
            '("MEDIUM-WE", 75, 62, "USD"),'
            '("LARGE-WE", 100, 90, "USD"),'
            '("EXTRA-LARGE-WE", 120, 111, "USD")'
        )
    )

    expected = [
        WardrobeElement("SMALL-WE", 50, 59, Currencies.USD),
        WardrobeElement("MEDIUM-WE", 75, 62, Currencies.USD),
        WardrobeElement("LARGE-WE", 100, 90, Currencies.USD),
        WardrobeElement("EXTRA-LARGE-WE", 120, 111, Currencies.USD)
    ]

    assert session.query(WardrobeElement).all() == expected