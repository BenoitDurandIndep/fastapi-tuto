from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel
from typing import Any,Union

app = FastAPI()

class BaseItem(BaseModel):
    description:str
    type:str
    name:str

class Item(BaseItem):
    price: float
    tax: float = 10.5
    tags: list[str] = []

class CarItem(Item):
    type="car"

class PlaneItem(Item):
    type="plane"
    size:int


class BaseUser(BaseModel):
    username: str
    email: str
    fullname: str | None = None


class UserIn(BaseUser):
    password: str


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

items2 = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}

@app.post("/items/")
async def create_items(item: Item) -> Item:
    return item


@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]

@app.get("/items2/{item_id}",response_model=Union[PlaneItem,CarItem])
async def read_item(item_id:str):
    return items[item_id]

@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user


@app.get("/portal/")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com")
    return JSONResponse(content={"message": "Here's your portal."})
