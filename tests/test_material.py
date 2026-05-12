import random
def test_create_material(authorized_api):

    payload={
        "name":f"Cotton_{random.randint(1000,9999)}"
    }

    response = authorized_api.post("/api/v1/business/material/create", json=payload)

    assert response.status_code == 200

def test_get_materials(authorized_api):

    response = authorized_api.get_materials(page=1, limit=5)
    limit = 5
    body = response.json()
    results = body["results"]

    assert response.status_code==200
    assert body["success"] is True
    assert "results" in body
    assert isinstance(results, list) 

def test_search_materials(authorized_api):

    response = authorized_api.get_materials(search="cotton", page=1, limit= 5)
    body = response.json()
    results = body["results"]

    assert response.status_code==200

    print(response)
    for item in results:
        assert "cotton" in item["name"].lower()

def test_get_material_category(authorized_api):

    response = authorized_api.get_materials(category_type="product")

    body = response.json()
    assert response.status_code==200
    assert body["success"] is True 