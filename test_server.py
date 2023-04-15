import requests as req

base_url = "http://127.0.0.1:8000/"

print("Getting items:")
print(req.get(base_url+"items/foo").json())

# print("Getting item 1 :")
# print(req.get(base_url+"items/1").json())


# print("Adding an item 1:")
# print(req.put(base_url+"items-create/1", json={
#     "name": "Item Ben",
#     "description": "A nice item from Ben",
#     "price": 34.3,
#     "tax": 3.23
# }).json())
