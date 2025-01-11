from fastapi import FastAPI
import json

app = FastAPI(title="Collekt Backend API",
    description="WIP",
    summary="API for the Collekt app.",
    version="0.0.1"
   )
from pydantic import BaseModel



class Offerings(BaseModel):
    wishlist_item_id: str
    price: float
    url: str

class WhishlistItem(BaseModel):
    id: str
    name: str
    description: str | None = None
    search_terms: list[str]
    offerings: list[Offerings] | None = None

class Wishlist(BaseModel):
    items: list[WhishlistItem]

item = WhishlistItem(id="fhfhf", name="item", description="moin", search_terms=["Moin", "Moin Moin"])

@app.get("/wishlist")
async def get_wishlist() -> Wishlist:
    print({"items": [item.dict()]})
    return {"items": [item.dict()]}

@app.post("/wishlist")
async def add_item_to_wishlist(item: WhishlistItem) -> WhishlistItem:
    return item

@app.put("/wishlist")
async def update_wishlist(item: WhishlistItem) -> WhishlistItem:
    return item

@app.delete("/wishlist")
async def delete_wishlist() -> WhishlistItem:
    return item

@app.get("/offerings/{item_id}")
async def get_item(item_id: str) -> Offerings:
    return item