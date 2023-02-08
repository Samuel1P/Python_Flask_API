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

@app.post("/store")
def add_stores():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items":[]}
    stores.append(new_store)
    return new_store, 201
    
    
app.run(port=8000)