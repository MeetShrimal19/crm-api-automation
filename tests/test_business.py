from api.business_api import BusinessAPI
import os
import random
from utils.logger import get_logger

logger = get_logger()
base_url = os.getenv("BASE_URL")


def test_create_business(auth_token):
    api = BusinessAPI(base_url)
    api.set_token(auth_token)
    name = "meet_"+str(random.randint(999,9999))
    email = "shrimalmeet" + str(random.randint(999,9999))+"@gmail.com"
    mobile_number = str(random.randint(1000000000,9999999999))
    logger.info(f"Creating business with name: {name}, email: {email}, mobile: {mobile_number}")
    response = api.create_business_management(name=name, email=email, address="heerabgh colony", mobile_code="+91", mobile_number=mobile_number)
    logger.info(f"Create business response code: {response.status_code}")
    assert response.status_code==201

def test_get_business(auth_token):
    api = BusinessAPI(base_url)
    api.set_token(auth_token)
    logger.info("Fetching business details (page=1, limit=5)")
    response = api.get_business_details(page=1, limit=5)
    logger.info(f"Get business response code: {response.status_code}")
    assert response.status_code==200

def test_business_by_id(auth_token):
    api = BusinessAPI(base_url)
    api.set_token(auth_token)
    business_id = "5"
    logger.info(f"Fetching business by ID: {business_id}")
    response = api.fetch_business_by_id(id=business_id)
    logger.info(f"Fetch business by ID response code: {response.status_code}")
    assert response.status_code==200

def test_update_businessId(auth_token):
    api=BusinessAPI(base_url)
    api.set_token(auth_token)
    businessId=1
    logger.info(f"Updating business ID: {businessId}")
    response = api.update_business_id(businessId)
    logger.info(f"Update business response code: {response.status_code}")
    assert response.status_code==200
