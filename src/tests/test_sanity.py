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
    store_name = uuid.uuid4().hex[:10]
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
