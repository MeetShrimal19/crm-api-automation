import random
import os
from api.contacts_api import ContactAPI
from api.auth_api import AuthAPI
from utils.logger import get_logger

logger = get_logger()
base_url = os.getenv("BASE_URL")


def test_add_customers(auth_token):
    api = ContactAPI(base_url)
    api.set_token(auth_token)
    logger.info("Created random variables for Name, Email, and Phone number")
    name = "Meet_"+ str(random.randint(999, 10000))
    email= f"meet{random.randint(1000000000, 9999999999)}@gmail.com"
    phone_number= str(random.randint(1000000000, 9999999999))

    logger.info(f"Adding contact with name: {name}, email: {email}, phone: {phone_number}")
    response = api.add_contact(name=name, email=email, mobile_code="+91", phone_number=phone_number, message="I am creating a contact")
    
    logger.info(f"Response status code: {response.status_code}")
    assert response.status_code== 201

def test_get_all_contacts(auth_token):
    api = ContactAPI(base_url)
    api.set_token(auth_token)

    logger.info("Fetching all contacts with page=1, limit=5")
    response = api.get_all_contacts(page =1, limit = 5)
    
    logger.info(f"Response status code: {response.status_code}")
    assert response.status_code == 200
