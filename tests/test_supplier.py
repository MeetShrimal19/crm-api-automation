import random
def test_create_supplier(auth_api,auth_token):
    endpoint="/api/v1/business/supplier/create"
    headers={
        "Authorization":f"Bearer {auth_token}"
    }

    random_phone = str(random.randint(6000000000, 9999999999))
    payload={
        "name":"meet shrimal",
        "phone":random_phone    
    }


    response = auth_api.post(endpoint, headers=headers, json=payload)
    body = response.json()

    assert response.status_code==201

    assert body["success"] is True 
    assert body["message"] == "Supplier added successfully"

def test_supplier_pagination(auth_api, auth_token):
    headers={
        "Authorization":f"Bearer {auth_token}"
    }

    response = auth_api.get_supplier(page=1, limit=3, headers=headers)
    limit = 3
    body = response.json()
    results = body["results"]["data"]

    assert response.status_code == 200
    assert body["success"] is True 
    assert body["message"] == "Suppliers fetched successfully"
    assert "results" in body
    assert len(results) <= limit 
    print("result length", len(results))
    print(limit)


def test_update_supplier(auth_api, auth_token):
    headers={
        "Authorization":f"Bearer {auth_token}"
    }
    supplier_id= 2555

    payload={
        "name": "Meet Shrimal"
    }

    response = auth_api.update_supplier(supplier_id, payload, headers=headers)
    body=response.json()

    assert response.status_code == 200
    assert body["success"] is True 

def test_updated_supplier(auth_api, auth_token):
    headers={
        "Authorization": f"Bearer {auth_token}"
    }
    random_phone = str(random.randint(6000000000, 9999999999))
    create_payload={
        "name":"new supplier",
        "phone": random_phone
    }

    create_response = auth_api.post("/api/v1/business/supplier/create", headers=headers, json=create_payload)
    assert create_response.status_code==201
    supplier_id = create_response.json()["results"]["supplier_id"]

    update_payload={
        "name":"Jaggu Shrimal"
    }
    updated_response=auth_api.update_supplier(supplier_id, update_payload,headers=headers)
    assert updated_response.status_code==200
    
    get_response = auth_api.get_supplier(limit=100, headers=headers)
    results = get_response.json()["results"]["data"]

    updated = False
    for item in results:
        if item["supplier_id"]==supplier_id:
            assert item["name"]== "Jaggu Shrimal"
            updated = True
    assert updated is True

def test_delete_supplier(auth_api, auth_token):

    headers={
            "Authorization":f"Bearer {auth_token}"
            }
    phone_number = random.randint(6000000000, 9999999999)
    create_payload={
            "name":"Vinoth",
            "phone":str(phone_number)
        }
        
    create_response = auth_api.post("/api/v1/business/supplier/create", headers=headers, json=create_payload)
    supplier_id = create_response.json()["results"]["supplier_id"]              

    delete_resource = auth_api.delete_supplier(supplier_id,headers=headers)
    assert delete_resource.status_code==200

    get_result= auth_api.get_supplier(page=1, limit =10, headers=headers)
    results = get_result.json()["results"]

    found = False
    for item in results:
        if isinstance(item, dict) and item["supplier_id"] == supplier_id:
            found = True

    assert found is False

