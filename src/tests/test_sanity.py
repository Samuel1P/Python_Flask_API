import pytest
import requests
import uuid

endpoint = "http://127.0.0.1:8000/"

def test_app_health():
    resp = requests.get(endpoint+"health")
    assert "good" in resp.text
    assert resp.status_code == 200

def test_say_hello():
    name = "sam"
    resp = requests.get(endpoint+"say_hello"+"/"+name)
    assert resp.status_code == 200
    print(resp.text)
    assert "Hello, {}".format(name) in resp.text

def test_get_store():
    resp = requests.get(endpoint+"store")
    assert resp.status_code == 200
    
def test_create_store():
    store_name = "dummy_store"
    new_store_payload = {"name": store_name}
    resp = requests.post(endpoint+"store", json=new_store_payload)
    assert resp.status_code == 201
    resp2 = requests.get(endpoint+"store")
    assert resp2.status_code == 200
    store_data = resp2.json()
    for store in store_data["stores"]:
        if store["name"]==store_name:
            assert True
            break
    else:
        assert False, "Did not find store {}".format(store_name)

def test_add_item_to_store():
    store_name = "dummy_store"
    new_store_payload = {"name": store_name}
    resp = requests.post(endpoint+"store", json=new_store_payload)
    assert resp.status_code == 201
    resp2 = requests.get(endpoint+"store")
    assert resp2.status_code == 200
    store_data = resp2.json()
    for store in store_data["stores"]:
        if store["name"]==store_name:
            assert True
            break
    else:
        assert False, "Did not find store {}".format(store_name)
    # test starts here
    item_to_add = {"items":{"name": "Coconut Oil",
                   "mrp": 50.0,
                   "quantity": "1 litre"}}
    resp3 = requests.put(endpoint+"store"+"/"+store_name, json=item_to_add)
    assert resp3.status_code == 200
    resp4 = requests.get(endpoint+"store"+"/"+store_name)
    store_data = resp4.json()
    print(store_data)
    assert store_data["name"]==store_name
    for item in store_data["items"]:
        print (item_to_add["items"]["name"], item["name"])
        if item_to_add["items"]["name"] == item["name"]:
            assert True
            break
    else:
        assert False, "New item not found."
    
    