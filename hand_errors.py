from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse


class UnicornException(Exception):
    def __init__(self, name: str) -> None:
        self.name = name


app = FastAPI()


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(status_code=418, content={"message": f"Oups ! {exc.name} did something. go rainbow"},)

items = {"foo": "The Foo Wrestlers"}


@ app.get("/items/{item_id}")
async def read_items(item_id: str):
    if item_id=="yolo":
        raise UnicornException(name=item_id)
    elif item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found", headers={
                            "X-Error": "My error"})
    return {"item": items[item_id]}
