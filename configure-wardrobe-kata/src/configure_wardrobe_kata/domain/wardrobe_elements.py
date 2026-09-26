from dataclasses import dataclass

from configure_wardrobe_kata.domain.currencies import Currencies


@dataclass
class SmallWE:
    length: int = 50
    price: int = 59
    currency: Currencies = Currencies.USD


@dataclass
class MediumWE:
    length: int = 75
    price: int = 62
    currency: Currencies = Currencies.USD


@dataclass
class LargeWE:
    length: int = 100
    price: int = 90
    currency: Currencies = Currencies.USD


@dataclass
class ExtraLargeWE:
    length: int = 120
    price: int = 111
    currency: Currencies = Currencies.USD