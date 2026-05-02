import random
def test_create_material(auth_api, auth_token):
    headers={
        "Authorization": f"Bearer {auth_token}",
        "Content-Type":"application/json"
    }

    payload={
        "name":f"Cotton_{random.randint(1000,9999)}"
    }

    response = auth_api.post("/api/v1/business/material/create", headers=headers, json=payload)

    assert response.status_code == 200

def test_get_materials(auth_api, auth_token):
    headers ={
        "Authorization":f"Bearer {auth_token}"
    }

    response = auth_api.get_materials(page=1, limit=5, headers=headers)
    limit = 5
    body = response.json()
    results = body["results"]

    assert response.status_code==200
    assert body["success"] is True
    assert "results" in body
    assert isinstance(results, list) 

def test_search_materials(auth_api, auth_token):
    headers={
        "Authorization": f"Bearer {auth_token}"
    }

    response = auth_api.get_materials(search="cotton", headers=headers, page=1, limit= 5)
    body = response.json()
    results = body["results"]

    assert response.status_code==200

    print(response)
    for item in results:
        assert "cotton" in item["name"].lower()

def test_get_material_category(auth_api,auth_token):
    headers={
        "Authorization":f"Bearer {auth_token}"
    }

    response = auth_api.get_materials(category_type="product", headers=headers)

    body = response.json()
    assert response.status_code==200
    assert body["success"] is True 