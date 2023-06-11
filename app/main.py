from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles


from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users

app = FastAPI(dependencies=[Depends(get_query_token)])

app.mount("/static", StaticFiles(directory="static",
          check_dir=False), name="static")


app.include_router(users.router)
app.include_router(items.router)
app.include_router(admin.router, prefix="/admin", tags=["admin"], dependencies=[
                   Depends(get_token_header)], responses={418: {"description": "I'm a mug"}},)


@app.get("/")
async def root():
    return {"message": "Hello Big App"}
