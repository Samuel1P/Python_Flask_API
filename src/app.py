from crypt import methods
from operator import methodcaller
from flask import Flask

app = Flask(__name__)


@app.route("/store", methods=["POST"])
def create_store():
    return "POST: Hello, World!"

@app.route("/store/<string:name>", methods=["GET"])
def get_store(name):
    return "GET"

@app.route("/store", methods=["GET"])
def get_stores():
    return "GET: Hello, World!"

@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    return "POST: Item"

@app.route("/store/<string:name>/item", methods=["GET"])
def get_item_in_store(name):
    return "GET: Item"

app.run(port=8000)