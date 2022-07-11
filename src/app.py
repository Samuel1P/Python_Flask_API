import json
from flask import Flask, jsonify, request, render_template

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

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route("/store", methods=["GET"])
def get_stores():
    return jsonify({"stores": stores})


@app.route("/store/<string:name>", methods=["GET"])
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({"message": "NOT FOUND"})


@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "mrp": request_data["mrp"], "quantity": request_data["quantity"]}
            store["items"].append(new_item)
            return jsonify({"items": store["items"]})
    return jsonify({"message": "NOT FOUND"})


@app.route("/store/<string:name>/item", methods=["GET"])
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"items": store["items"]})
    return jsonify({"message": "NOT FOUND"})


app.run(port=8000)