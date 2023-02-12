from flask import Flask, request


app = Flask(__name__)


stores = [
    {
        "name": "Grocery_Store",
        "items": [
            {
                "name" : "Saffola Cooking Oil",
                "mrp" : 120.0,
                "quantity": "1 Litre"
            }
        ]
        
    },
    {
        "name": "Electrical_Store",
        "items": [
            {
                "name" : "Copper Wire",
                "mrp" : 120.0,
                "quantity": "1 Meter"
            }
        ] 
    }
]


@app.get("/health")
def health():
    return f"Well and good."

@app.get("/say_hello/<name>")
def hello(name):
    return f"Hello, {name}!"

@app.get("/store")
def get_stores():
    return {"stores": stores}

@app.get("/store/<store_name>")
def get_single_store(store_name):
    for store in stores:
        if store["name"] ==store_name: 
            return store, 200
    else:
        return {"Error": "Store Not Found"}, 400

@app.post("/store")
def add_stores():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items":[]}
    stores.append(new_store)
    return new_store, 201


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

app.run(port=8000)