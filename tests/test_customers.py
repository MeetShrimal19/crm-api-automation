import os
from api.customer_api import CustomerAPI

base_url = os.getenv('BASE_URL')
import random 
from utils.logger import get_logger
logger = get_logger()
def test_post_customers(auth_token):
    authorized_api = CustomerAPI(base_url)
    authorized_api.set_token(auth_token)
    logger.info("Created random variables for Name and Phone number")
    random_name = "Meet_" + str(random.randint(1000,9999))
    random_phonenumber = "89"+ str(random.randint(100000, 999999999))
    logger.info(f"Adding customer with name: {random_name} and phone: {random_phonenumber}")
    response = authorized_api.post_customers(random_name, "chennai", random_phonenumber)

    logger.info(f"Response status code: {response.status_code}")
    assert response.status_code == 201

    logger.info("checking the response of the API")
    data = response.json()
    assert data["success"] == True 
    assert data["message"] == "Customer added successfully"
    assert data["results"]["customer"]["name"] == random_name
    assert data["results"]["customer"]["area"] == "chennai"
    assert data["results"]["customer"]["contact_number"] == random_phonenumber

def test_get_all_customers(auth_token):
    authorized_api = CustomerAPI(base_url)
    authorized_api.set_token(auth_token)
    logger.info("Fetching all customers info with page=1, limit=5, customer_name='meet shrimal'")
    response = authorized_api.all_customer_info(page = 1, limit = 5, customer_name="meet shrimal")
    logger.info(f"Response status code: {response.status_code}")
    assert response.status_code == 200
    logger.info("Checking the response data of the API")
    data = response.json()
    assert data["success"]== True 
    assert data["code"]== 200
    assert data["message"] == 'Customer retrieved successfully'

def test_update_customers(auth_token):
    authorized_api = CustomerAPI(base_url)
    authorized_api.set_token(auth_token)
    logger.info("Fetching all customers to select a random customer for update")
    response_get_customer = authorized_api.all_customer_info(page=1, limit=5)
    customer_data= response_get_customer.json()
    customer_list = customer_data["results"]["data"]
    random_customer = random.choice(customer_list)
    customer_id= random_customer["id"]
    logger.info(f"Selected random customer with id: {customer_id}")

    logger.info(f"Updating customer {customer_id} with new name, area, and contact_number")
    response = authorized_api.update_customers(customerId=customer_id, name="meet shrimal", area="chennai", contact_number="8955251538")
    logger.info(f"Response status code: {response.status_code}")
    assert response.status_code == 200
    logger.info("Checking the response data of the API")
    data = response.json()
    assert data["success"]==True
    assert data["message"] == "Customer Updated successfully"

def test_delete_customer(auth_token):
    authorized_api = CustomerAPI(base_url)
    authorized_api.set_token(auth_token)
    logger.info("Fetching all customers to select a random customer for deletion")
    get_customer_response = authorized_api.all_customer_info(page=1, limit=5)
    assert get_customer_response.status_code == 200
    data = get_customer_response.json()
    customer_list = data["results"]["data"]
    random_customer = random.choice(customer_list)
    customer_id = random_customer["id"]
    logger.info(f"Selected random customer for deletion with id: {customer_id}")

    logger.info(f"Deleting customer with id: {customer_id}")
    response = authorized_api.delete_customer(customer_id=customer_id)
    logger.info(f"Response status code: {response.status_code}")
    assert response.status_code == 200
    logger.info("Checking the response data of the API")
    delete_data = response.json()
    assert delete_data["success"] == True
    assert delete_data["message"]== "Customer deleted successfully"


    