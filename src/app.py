import uuid
from flask import Flask, request
from flask_smorest import abort
from db import items, stores

app = Flask(__name__)
gen_uuid = lambda :uuid.uuid4().hex[:8]

@app.get("/health")
def health():
    return f"Well and good."

@app.get("/hello/<string:name>")
def hello(name):
    return f"Hello, {name}!"

@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}

@app.get("/store/<string:store_id>")
def get_single_store(store_id):
    if stores.get(store_id):
        return stores[store_id], 200
    abort(404, message= {"Error": "Store {} Not Found.".format(store_id)})

@app.post("/store")
def create_stores():
    request_data = request.get_json()    
    new_uuid = gen_uuid()
    new_store = {"name": request_data["name"],
                 "items_ids": request_data.get("items", list()),
                 "store_id": new_uuid}
    stores[new_uuid]=new_store
    return new_store, 201

@app.get("/items")
def get_items():
    return {"items": list(items.values())}

@app.get("/items/<string:item_id>")
def get_single_item(item_id):
    if items.get(item_id):
        return items[item_id], 200
    abort(404, message={"Error": "Item {} Not Found.".format(item_id)}) 

@app.post("/items")
def create_item():
    request_data = request.get_json()
    new_uuid = gen_uuid()
    new_item_data = request_data
    new_item = {"item_id": new_uuid,
                "name": new_item_data["name"]}
    items[new_uuid]=new_item
    return new_item, 201

"""
@app.put("/store/<store_name>")
def add_item_to_store(store_name):
    request_data = request.get_json()
    new_item = request_data["items"]
    print(new_item)
    for store in stores:
        if store["name"] ==store_name:
            print(store["name"], store_name) 
            store["items"].append(new_item)
            return store, 200
    else:
        return {"Error": "Store Not Found"}, 400 

@app.get("/store/<store_name>/<item_name>")
def get_item_from_store(store_name, item_name):
    item = ""
    for store in stores:
        if store["name"] ==store_name:
            print(store["name"], store_name) 
            items_in_target_store = store["items"]
            break
    else:
        return {"Error": "Store {} Not Found".format(store_name)}, 404 
    for item in items_in_target_store:
        if item["name"] == item_name:
            return item, 200
    else:
        return {"Error": "Item {} Not Found".format(item_name)}, 404  
"""

app.run(port=8000)