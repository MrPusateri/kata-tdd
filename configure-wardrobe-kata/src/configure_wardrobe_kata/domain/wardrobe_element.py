from dataclasses import dataclass

from configure_wardrobe_kata.domain.currencies import Currencies

@dataclass(unsafe_hash=True)
class WardrobeElement:
    length: int
    price: int
    currency: Currencies
