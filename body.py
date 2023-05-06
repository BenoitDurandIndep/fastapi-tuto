from enum import Enum
from typing import Annotated
from fastapi import FastAPI, Path, Body
from pydantic import BaseModel, Field, HttpUrl

# https://fastapi.tiangolo.com/tutorial/body-multiple-params/

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description", max=300)
    price: float = Field(gt=0, description="Price of the item greater than 0")
    tax: float | None = None
    tags: set[str] = set()
    image: list[Image] | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]

class Tags(Enum):
    items = "items"
    users = "users"

@app.put("/items/{item_id}",tags=[Tags.items])
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


@app.put("/items_user/{item_id}",tags=[Tags.items])
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)], user: User, importance: Annotated[int, Body()]):
    results = {"item_id": item_id, "item": item,
               "user": user, "importance": importance}
    return results

@app.post("/images/multiple/")
async def create_multiple_images(images:list[Image]):
    return images

@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer

@app.post("/index-weights/")
async def create_index_weights(weights: dict[int,float]):
    return weights
