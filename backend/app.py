from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry import trace

# Define the service name
resource = Resource.create({"service.name": "collekt"})

# Set up the Tracer Provider
provider = TracerProvider(resource=resource)

# Configure OTLP Exporter (sends traces to Jaeger)
otlp_exporter = OTLPSpanExporter(endpoint="http://jaeger:4317", insecure=True)

# Add the OTLP exporter to the TracerProvider
span_processor = BatchSpanProcessor(otlp_exporter)
provider.add_span_processor(span_processor)

# Set the global TracerProvider
trace.set_tracer_provider(provider)

app = FastAPI(
    title="Collekt Backend API",
    description="WIP",
    summary="API for the Collekt app.",
    version="0.0.1"
)

# Automatically instrument FastAPI
FastAPIInstrumentor.instrument_app(app)

class Offerings(BaseModel):
    wishlist_item_id: str
    title: str
    price: float
    url: str

class WishlistItem(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    search_terms: List[str]
    offerings: Optional[List[Offerings]] = None

class Wishlist(BaseModel):
    items: List[WishlistItem] = []

# In-Memory-Database
# TODO: Replace with a real database
wishlist = Wishlist(items=[])

@app.get("/wishlist", response_model=Wishlist)
async def get_wishlist():
    return wishlist

@app.get("/wishlist/{item_id}", response_model=WishlistItem)
async def get_wishlist_item(item_id: str):
    for item in wishlist.items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/wishlist", response_model=WishlistItem)
async def add_item_to_wishlist(item: WishlistItem):
    # Check if the item already exists
    for existing_item in wishlist.items:
        if existing_item.id == item.id:
            raise HTTPException(status_code=400, detail="Item with this ID already exists")
    wishlist.items.append(item)
    return item

@app.delete("/wishlist/{item_id}")
async def delete_wishlist_item(item_id: str):
    for index, item in enumerate(wishlist.items):
        if item.id == item_id:
            del wishlist.items[index]
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/offerings/{item_id}", response_model=List[Offerings])
async def get_offerings(item_id: str) -> List[Offerings]:
    for item in wishlist.items:
        if item.id == item_id:
            # Please note that this is a mock implementation
            return [{"wishlist_item_id": item_id, "title": "1989 (TAYLORS VERSION) CRYSTAL SKIES BLUE CD", "price": 19.97, "url": "https://www.amazon.de/1989-Taylors-Version-Chrystal-Skies/dp/B0CFM76QSG"}]
    raise HTTPException(status_code=404, detail="Item not found or no offerings available")
