from typing import Annotated

from fastapi import FastAPI, Form, File, UploadFile

app = FastAPI()


@app.post("/login/")
async def login(username: Annotated[str, Form()], passwordusername: Annotated[str, Form()]):
    return {"username", username}

# stored on memory


@app.post("/files/")
async def create_file(file: Annotated[bytes | None, File(description="A file read as bytes")] = None):
    return {"file_size": len(file)}

# stored on disk


@app.post("/uploadfile/")
async def create_upload_file(file: Annotated[UploadFile | None, File(description="A file read as Upload file")] = None):
    return {"filename": file.filename}
