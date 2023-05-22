import requests as req

base_url = "http://127.0.0.1:8000/"

# print("Getting items:")
# print(req.get(base_url+"items/foo").json())

# print("Getting item 1 :")
# print(req.get(base_url+"items/foo").json())
# print(req.get(base_url+"items/yolo").json())

# print("Posting items :")
# rep=req.post(base_url+"items", json={
#     "name": "Item Ben",
#     "description": "A nice item from Ben",
#     "price": 34.3
# })
# print(f"{rep.status_code=}, {rep.json()=}")

# print("Adding an item toto:")
# print(req.put(base_url+"items/toto", json={
#     "name": "Item Ben",
#     "description": "A nice item from Ben",
#     "price": 34.3,
#     "tax": 3.23
# }).json())

print("Update an item bar:")
print(req.put(base_url+"items/bar", json={
    "name": "New Bar",
    "description": "A nice new bar from Ben",
    "price": 34.3
}).json())
