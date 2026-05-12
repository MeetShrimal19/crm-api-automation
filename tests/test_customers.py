import random 
import logging
logger = logging.getLogger(__name__)
def test_post_customers(authorized_api):
    logger.info("Created random variables for Name and Phone number")
    random_name = "Meet_" + str(random.randint(1000,9999))
    random_phonenumber = "89"+ str(random.randint(100000, 999999999))
    response = authorized_api.post_customers(random_name, "chennai", random_phonenumber)

    assert response.status_code == 201

    logger.info("checking the response of the API")
    data = response.json()
    assert data["success"] == True 
    assert data["message"] == "Customer added successfully"
    assert data["results"]["customer"]["name"] == random_name
    assert data["results"]["customer"]["area"] == "chennai"
    assert data["results"]["customer"]["contact_number"] == random_phonenumber

def test_get_all_customers(authorized_api):

    response = authorized_api.all_customer_info(page = 1, limit = 5, customer_name="meet shrimal")
    assert response.status_code == 200
    data = response.json()
    assert data["success"]== True 
    assert data["code"]== 200
    assert data["message"] == 'Customer retrieved successfully'

def test_update_customers(authorized_api):

    response_get_customer = authorized_api.all_customer_info(page=1, limit=5)
    customer_data= response_get_customer.json()
    customer_list = customer_data["results"]["data"]
    random_customer = random.choice(customer_list)
    customer_id= random_customer["id"]


    response = authorized_api.update_customers(customerId=customer_id, name="meet shrimal", area="chennai", contact_number="8955251538")
    assert response.status_code == 200
    data = response.json()
    assert data["success"]==True
    assert data["message"] == "Customer Updated successfully"
    