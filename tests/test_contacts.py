import random
import logging

logger = logging.getLogger(__name__)

def test_post_customers(authorized_api):
    logger.info("Created random variables for Name, Email, and Phone number")
    name = "Meet_"+ str(random.randint(999, 10000))
    email= f"meet{random.randint(1000000000, 9999999999)}@gmail.com"
    phone_number= str(random.randint(1000000000, 9999999999))

    logger.info(f"Adding contact with name: {name}, email: {email}, phone: {phone_number}")
    response = authorized_api.add_contact(name=name, email=email, mobile_code="+91", phone_number=phone_number, message="I am creating a contact")
    
    logger.info(f"Response status code: {response.status_code}")
    assert response.status_code== 201

def test_get_all_contacts(authorized_api):
    logger.info("Fetching all contacts with page=1, limit=5")
    response = authorized_api.get_all_contacts(page =1, limit = 5)
    
    logger.info(f"Response status code: {response.status_code}")
    assert response.status_code == 200
