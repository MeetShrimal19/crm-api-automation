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
    results = body["results"]

    assert response.status_code == 200
    assert body["success"] is True 
    assert body["message"] == "Suppliers fetched successfully"
    assert "results" in body
    assert len(results) <= limit 
    print("result length", len(results))
    print(limit)



