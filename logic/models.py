from dataclasses import dataclass

@dataclass
class Offerings():
    wishlist_item_id: str
    price: float
    url: str


@dataclass
class WishlistItem():
    id: str
    name: str
    search_terms: list[str]
    description: str | None = None
    offerings: list[Offerings] | None = None

@dataclass
class Wishlist():
    items: list[WishlistItem]
