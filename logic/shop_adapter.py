from db_handler import DBHandler

class ShopAdapter:

    def __init__(self):
        self.db_handler = DBHandler()

    def search_offers(self) -> list[str]:
        wishlist = self.db_handler.get_wishlist()
        wishlist_items = wishlist.items
        search_terms = [item.search_terms for item in wishlist_items]
        return search_terms