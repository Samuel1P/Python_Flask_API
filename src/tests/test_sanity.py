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
        resp = requests.get(endpoint+"hello"+"/"+name)
        assert resp.status_code == 200
        print(resp.text)
        assert "Hello, {}".format(name) in resp.text

    def test_get_all_stores(self):
        resp = requests.get(endpoint+"store")
        assert resp.status_code == 200
        
    def test_get_store(self, create_dummy_store):
        store_data = create_dummy_store
        expected_store_name = store_data["name"] 
        expected_store_id = store_data["store_id"] 
        resp2 = requests.get(endpoint+"store"+"/"+expected_store_id)
        assert resp2.status_code == 200
        actual_store_data= resp2.json()
        actual_store_name = actual_store_data["name"] 
        actual_store_id = actual_store_data["store_id"]
        assert expected_store_name == actual_store_name
        assert expected_store_id == actual_store_id
        
    def test_create_store(self):
        store_name = "dummy_store_create"
        new_store_payload = {"name": store_name}
        resp = requests.post(endpoint+"store", json=new_store_payload)
        store_data = resp.json()
        actual_store_name = store_data["name"]     
        assert resp.status_code == 201
        assert store_name == actual_store_name
        
    def test_get_absent_store(self):
        store_id = "non_existent_store_id"
        resp2 = requests.get(endpoint+"store"+"/"+store_id)
        assert resp2.status_code == 404
        
    def test_get_all_items(self):
        resp = requests.get(endpoint+"store")
        assert resp.status_code == 200
        
    def test_create_item(self, ):
        item_name = "dummy_item_create"
        new_item_payload = {"name": item_name}
        resp = requests.post(endpoint+"items", json=new_item_payload)
        item_data = resp.json()
        actual_item_name = item_data["name"]     
        assert resp.status_code == 201
        assert item_name == actual_item_name

    def test_get_item(self,create_dummy_item):
        item_data = create_dummy_item
        expected_item_name = item_data["name"] 
        expected_item_id = item_data["item_id"] 
        resp2 = requests.get(endpoint+"items"+"/"+expected_item_id)
        assert resp2.status_code == 200
        actual_item_data= resp2.json()
        actual_item_name = actual_item_data["name"] 
        actual_item_id = actual_item_data["item_id"]
        assert expected_item_name == actual_item_name
        assert expected_item_id == actual_item_id
        
    def test_get_absent_item(self):
        store_id = "non_existent_item_id"
        resp2 = requests.get(endpoint+"items"+"/"+store_id)
        assert resp2.status_code == 404
"""
    
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
        store_name, item = dummy_store_with_item
        item_name = item["name"]
        resp3 = requests.get(endpoint+"store"+"/"+store_name+"/"+item_name)
        assert resp3.status_code == 200
        item_from_server = resp3.json()
        assert item_from_server["name"] == "Coconut Oil"
        assert item_from_server["mrp"] == 50.0
        assert item_from_server["quantity"] == "1 litre"
        
"""