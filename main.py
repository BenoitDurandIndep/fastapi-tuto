from fastapi import FastAPI,Path,  Query
from enum import Enum
from pydantic import BaseModel
from typing import Annotated


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]


@ app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


@ app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "have some residuals"}


@ app.get("/items/me")
async def readm_me():
    return {"item": "my item"}


@ app.get("/users/{user_id}/items/{item_id}")
async def read_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "An amazing item !"})
    return item


@ app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "An amazing item !"})
    return item


@app.get("/items_list/")
async def read_items(q: Annotated[list, Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items


@app.get("/items3/")
# ... to default value if value is required
async def read_items(q: Annotated[str | None, Query(title="Query string",
                                                    description="Query string for the items to search in the db",
                                                    alias="item-query", min_length=3, max_length=50, deprecated=True, include_in_schema=False)] = "fixedquery"):

    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@ app.get("/items2/{item_id}")
async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    item_id = {"item_id": item_id, "needy": needy,
               "skip": skip, "limit": limit}
    return item_id


@ app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip:skip+limit]


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price+item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


@ app.get("/")
async def root():
    return {"message": "Hello World"}
