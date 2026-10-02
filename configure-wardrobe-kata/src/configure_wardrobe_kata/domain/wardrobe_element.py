from __future__ import annotations

from configure_wardrobe_kata.domain.currencies import Currencies


class WardrobeElement:

    def __init__(self, we_id: str, length: int, price: int, currency: Currencies):
        self.we_id = we_id
        self.length = length
        self.price = price
        self.currency = currency

    def __repr__(self):
        return f"<WardrobeElement {self.we_id}>"

    def __hash__(self):
        return hash(self.we_id)

    def __eq__(self, other):
        if not isinstance(other, WardrobeElement):
            return False

        return other.we_id==self.we_id

    def __lt__(self, other: WardrobeElement):
        return other.length > self.length
