from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import registry

from configure_wardrobe_kata.domain.wardrobe_element import WardrobeElement


mapper_registry = registry()
metadata = mapper_registry.metadata

wardrobe_catalog = Table(
    "wardrobe_catalog",
    metadata,
    Column("we_id", String(255), primary_key=True),
    Column("length", Integer, nullable=False),
    Column("price", Integer, nullable=False),
    Column("currency", String(3), nullable=False),
)

def start_mappers():
    wardrobe_catalog_mapper = mapper_registry.map_imperatively(WardrobeElement, wardrobe_catalog)