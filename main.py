from fastapi import FastAPI

app = FastAPI()


@app.get("/items/me")
async def readm_me():
    return {"item": "my item"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
