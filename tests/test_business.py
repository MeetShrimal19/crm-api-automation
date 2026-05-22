from api.business_api import BusinessAPI
import os
import random
base_url = os.getenv("BASE_URL")


def test_create_business(auth_token):
    api = BusinessAPI(base_url)
    api.set_token(auth_token)
    name = "meet_"+str(random.randint(999,9999))
    email = "shrimalmeet" + str(random.randint(999,9999))+"@gmail.com"
    mobile_number = str(random.randint(1000000000,9999999999))
    response = api.create_business_management(name=name, email=email, address="heerabgh colony", mobile_code="+91", mobile_number=mobile_number)
    assert response.status_code==201

def test_get_business(auth_token):
    api = BusinessAPI(base_url)
    api.set_token(auth_token)
    response = api.get_business_details(page=1, limit=5)
    assert response.status_code==200

def test_business_by_id(auth_token):
    api = BusinessAPI(base_url)
    api.set_token(auth_token)
    response = api.fetch_business_by_id(id="5")
    assert response.status_code==200

def test_update_businessId(auth_token):
    api=BusinessAPI(base_url)
    api.set_token(auth_token)
    businessId=1
    params={
        "businessId":businessId
    }
    response = api.update_business_id(businessId)
    assert response.status_code==200
