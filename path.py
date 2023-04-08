from fastapi import FastAPI, Path,  Query
from typing import Annotated

#https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/
app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(item_id: Annotated[int, Path(title="The id of the item to get",ge=1, le=1000)],
                      size : Annotated[float,Query(gt=0,lt=10.5)],
                     q: Annotated[str | None, Query(alias="item-query")] = None):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
