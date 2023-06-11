from fastapi.testclient import TestClient

from .main import app

client=TestClient(app=app)

def test_read_main():
    response=client.get("/")
    assert response.status_code==200
    assert response.json()=={"msg":"Test Hello World"}

def test_read_item():
    response = client.get("/items/foo", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 404
    assert response.json() == {       "detail": "Item not found"    }