from api.brands_api import BrandsAPI
from api.auth_api import AuthAPI
import os

base_url = os.getenv("BASE_URL")

def test_get_brands(auth_token):
    api = BrandsAPI(base_url)
    api.set_token(auth_token)
    response = api.get_brand_list()
    assert response.status_code == 200
