import pytest
import requests
import uuid

url = "http://127.0.0.1"
port = "8000"
endpoint = url+":"+port+"/"

class Test_Store:

    def test_app_health(self):
        resp = requests.get(endpoint+"health")
        assert "good" in resp.text
        assert resp.status_code == 200

    def test_say_hello(self):
        name = "sam"
        resp = requests.get(endpoint+"say_hello"+"/"+name)
        assert resp.status_code == 200
        print(resp.text)
        assert "Hello, {}".format(name) in resp.text

    def test_get_all_stores(self):
        resp = requests.get(endpoint+"store")
        assert resp.status_code == 200
        
    def test_create_store(self, create_dummy_store):
        store_name= create_dummy_store
        resp2 = requests.get(endpoint+"store")
        assert resp2.status_code == 200
        store_data = resp2.json()
        for store in store_data["stores"]:
            if store["name"]==store_name:
                assert True
                break
        else:
            assert False, "Did not find store {}".format(store_name)

    
    def test_add_item_to_store(self, create_dummy_store):
        store_name = create_dummy_store
        resp2 = requests.get(endpoint+"store")
        assert resp2.status_code == 200
        # test starts here
        item_to_add = {"items":{"name": "Coconut Oil",
                    "mrp": 50.0,
                    "quantity": "1 litre"}}
        resp3 = requests.put(endpoint+"store"+"/"+store_name, json=item_to_add)
        assert resp3.status_code == 200
        resp4 = requests.get(endpoint+"store"+"/"+store_name)
        store_data = resp4.json()
        assert store_data["name"]==store_name
        for item in store_data["items"]:
            print (item_to_add["items"]["name"], item["name"])
            if item_to_add["items"]["name"] == item["name"]:
                assert True
                break
        else:
            assert False, "New item not found."
        
    def test_get_item_from_store(self, dummy_store_with_item):
        """
        {"items":{"name": "Coconut Oil",
                    "mrp": 50.0,
                    "quantity": "1 litre"}}
        """
        store_name, item = dummy_store_with_item
        item_name = item["name"]
        resp3 = requests.get(endpoint+"store"+"/"+store_name+"/"+item_name)
        assert resp3.status_code == 200
        item_from_server = resp3.json()
        assert item_from_server["name"] == "Coconut Oil"
        assert item_from_server["mrp"] == 50.0
        assert item_from_server["quantity"] == "1 litre"
        
