from api.brands_api import BrandsAPI
from api.auth_api import AuthAPI
import os
from utils.logger import get_logger

logger = get_logger()
base_url = os.getenv("BASE_URL")

def test_get_brands(auth_token):
    api = BrandsAPI(base_url)
    api.set_token(auth_token)
    logger.info("Fetching brand list from BrandsAPI")
    response = api.get_brand_list()
    logger.info(f"Brand list response status: {response.status_code}")
    assert response.status_code == 200
