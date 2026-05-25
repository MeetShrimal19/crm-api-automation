import os
from api.materials_api import MaterialAPi

base_url = os.getenv('BASE_URL')
import random
from utils.logger import get_logger

logger = get_logger()

def test_create_material(auth_token):
    authorized_api = MaterialAPi(base_url)
    authorized_api.set_token(auth_token)
    name = f"Cotton_{random.randint(1000,9999)}"
    payload={
        "name": name
    }
    logger.info(f"Creating material with name: {name}")

    response = authorized_api.post("/api/v1/business/material/create", json=payload)
    logger.info(f"Response status code: {response.status_code}")

    assert response.status_code == 200

def test_get_materials(auth_token):
    authorized_api = MaterialAPi(base_url)
    authorized_api.set_token(auth_token)
    logger.info("Fetching materials with page=1, limit=5")
    response = authorized_api.get_materials(page=1, limit=5)
    limit = 5
    
    logger.info(f"Response status code: {response.status_code}")
    body = response.json()
    results = body["results"]

    assert response.status_code==200
    assert body["success"] is True
    assert "results" in body
    assert isinstance(results, list) 

def test_search_materials(auth_token):
    authorized_api = MaterialAPi(base_url)
    authorized_api.set_token(auth_token)
    logger.info("Searching materials with search='cotton', page=1, limit=5")
    response = authorized_api.get_materials(search="cotton", page=1, limit= 5)
    
    logger.info(f"Response status code: {response.status_code}")
    body = response.json()
    results = body["results"]

    assert response.status_code==200

    logger.info(f"Validating that 'cotton' is in the names of all {len(results)} results")
    for item in results:
        assert "cotton" in item["name"].lower()

def test_get_material_category(auth_token):
    authorized_api = MaterialAPi(base_url)
    authorized_api.set_token(auth_token)
    logger.info("Fetching materials with category_type='product'")
    response = authorized_api.get_materials(category_type="product")

    logger.info(f"Response status code: {response.status_code}")
    body = response.json()
    assert response.status_code==200
    assert body["success"] is True 