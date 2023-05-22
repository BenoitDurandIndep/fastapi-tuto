from enum import Enum
from typing import Annotated
from fastapi import FastAPI, Path, Body
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, HttpUrl

# https://fastapi.tiangolo.com/tutorial/body-multiple-params/
# https://fastapi.tiangolo.com/tutorial/body-updates/

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description", max=300)
    price: float = Field(gt=0, description="Price of the item greater than 0")
    tax: float | None = 10.5
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

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.put("/items/{item_id}",tags=[Tags.items])
async def update_item(
    item_id: Annotated[str, Path(title="The ID of the item")],#Annotated[int, Path(title="The ID of the item", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        #results.update({"item": item})
        stored_item_data = items[item_id]
        stored_item_model=Item(**stored_item_data)
        update_data=item.dict(exclude_unset=True)
        updated_item=stored_item_model.copy(update=update_data)
        items[item_id]=jsonable_encoder(updated_item)
        results=items[item_id]
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
