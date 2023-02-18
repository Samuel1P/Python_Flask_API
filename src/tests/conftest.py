from pickletools import pybytes_or_str

import requests
from pytest import fixture
endpoint = "http://127.0.0.1:8000/"

@fixture
def create_dummy_store():
    store_name = "dummy_store"
    new_store_payload = {"name": store_name}
    resp = requests.post(endpoint+"store", json=new_store_payload)
    store_data = resp.json()    
    assert resp.status_code == 201
    return store_data

@fixture
def create_dummy_item():
    item_name = "dummy_item_create"
    new_item_payload = {"name": item_name}
    resp = requests.post(endpoint+"items", json=new_item_payload)
    item_data = resp.json()    
    assert resp.status_code == 201
    return item_data

@fixture
def dummy_store_with_item(create_dummy_store):
    store_name = create_dummy_store
    new_store_payload = {"name": store_name}
    resp = requests.post(endpoint+"store", json=new_store_payload)
    assert resp.status_code == 201
    item_to_add = {"items":{"name": "Coconut Oil",
                    "mrp": 50.0,
                    "quantity": "1 litre"}}
    resp3 = requests.put(endpoint+"store"+"/"+store_name, json=item_to_add)
    assert resp3.status_code == 200
    return store_name, item_to_add["items"]