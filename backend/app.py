from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from typing import List, Optional

app = FastAPI(
    title="Collekt Backend API",
    description="WIP",
    summary="API for the Collekt app.",
    version="0.0.1"
)

# Define the service name
resource = Resource.create({"service.name": "collekt"})

# Step 1: Set up the Tracer Provider
provider = TracerProvider(resource=resource)
trace.set_tracer_provider(provider)

# Step 2: Configure OTLP Exporter (sends traces to Jaeger)
otlp_exporter = OTLPSpanExporter(endpoint="http://jaeger:4317", insecure=True)

# Step 3: Add the OTLP exporter to the TracerProvider
span_processor = BatchSpanProcessor(otlp_exporter)
provider.add_span_processor(span_processor)

# Get a tracer
tracer = trace.get_tracer("collekt")

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

# In-Memory-Datenbank
wishlist = Wishlist(items=[])

@app.get("/wishlist", response_model=Wishlist)
async def get_wishlist():
    with tracer.start_as_current_span("get-wishlist-from-backend") as parent:
        parent.set_attribute("component", "frontend")
        time.sleep(0.12446)
        with tracer.start_as_current_span("request-wishlist-from-db") as child:
            child.set_attribute("component", "backend")
            time.sleep(0.132541)  # Simulating database fetch delay
            with tracer.start_as_current_span("db-processing") as child:
                child.set_attribute("component", "db")
                time.sleep(0.32541) 
            time.sleep(0.14446)
        time.sleep(0.14446)
        return wishlist

@app.get("/wishlist/{item_id}", response_model=WishlistItem)
async def get_wishlist_item(item_id: str):
    with tracer.start_as_current_span("get-wishlist-item") as parent:
        parent.set_attribute("custom-tag", "get-wishlist-item")

        for item in wishlist.items:
            if item.id == item_id:
                return item
        raise HTTPException(status_code=404, detail="Item not found")

@app.post("/wishlist", response_model=WishlistItem)
async def add_item_to_wishlist(item: WishlistItem):
    with tracer.start_as_current_span("add-item-to-wishlist") as parent:
        parent.set_attribute("custom-tag", "add-wishlist-item")
        
        # Check if the item already exists
        for existing_item in wishlist.items:
            if existing_item.id == item.id:
                raise HTTPException(status_code=400, detail="Item with this ID already exists")
        
        with tracer.start_as_current_span("add-item-to-db") as child:
            child.set_attribute("operation", "posting wishlist item")
            time.sleep(0.32541)  # Simulating database fetch delay
        
        # Add the item to the wishlist
        wishlist.items.append(item)
        
        # Return the newly added item
        return item


@app.delete("/wishlist/{item_id}")
async def delete_wishlist_item(item_id: str):
    with tracer.start_as_current_span("delete-wishlist-item") as parent:
        parent.set_attribute("custom-tag", "delete-wishlist-item")
        for index, item in enumerate(wishlist.items):
            if item.id == item_id:
                del wishlist.items[index]
                return {"message": "Item deleted"}
        raise HTTPException(status_code=404, detail="Item not found")

@app.get("/offerings/{item_id}", response_model=List[Offerings])
async def get_offerings(item_id: str) -> List[Offerings]:
    with tracer.start_as_current_span("get-offerings") as parent:
        parent.set_attribute("custom-tag", "get-offerings")
        for item in wishlist.items:
            if item.id == item_id:
                return [{"wishlist_item_id": item_id, "title": "1989 (TAYLORS VERSION) CRYSTAL SKIES BLUE CD", "price": 19.97, "url": "https://www.amazon.de/1989-Taylors-Version-Chrystal-Skies/dp/B0CFM76QSG/ref=sr_1_4_mod_primary_new?crid=2LWIL08LAEBML&dib=eyJ2IjoiMSJ9.SUMq_X88Q5YtKX8rU5T1905PUZIQ1dR8lueYhSD4eIFpPYuYdlqJL9L4dPM3XSBD8jniA0t_PcwlFoTsg6dwnU_8hgpTvRsxIBYMDtOJC-syAt7TLd2CIPKAOmavlJjndlS3hOVQ5WTkzQ6vBks1dAVHp1jl1b_U1UtEnVw9339bHjm8PzsGdYHXXTYTe4rEI4dzmeMWbFO2RV0A6X2el2_f9Agxz3uwYzJp5IiV3VY.-OUjXQQGIh8cY1ZbMSMp1M4UmXSWtyC95rBiIohFjX0&dib_tag=se"}]
        raise HTTPException(status_code=404, detail="Item not found or no offerings available")
