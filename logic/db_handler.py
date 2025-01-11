import requests
import os
from models import WishlistItem, Wishlist
from dotenv import load_dotenv

class DBHandler:

    
    #load_dotenv()

    def get_wishlist(self) -> Wishlist:
        host_name = os.environ["BACKEND_HOST_NAME"]
        response = requests.get(f"{host_name}:8000/wishlist")

        if response.status_code == 200:

            wishlist_json = response.json()
            wishlist = Wishlist(**wishlist_json)
            wishlist.items = [WishlistItem(**item) for item in wishlist_json.get("items", [])]
            return wishlist

        else:
            print(f"Failed with status code: {response.status_code}")