from utils.logger import get_logger

logger = get_logger()

def test_send_otp(authorized_api):
    email="shrimalmeet2001@gmail.com"
    logger.info(f"Sending OTP to email: {email}")
    response = authorized_api.send_otp(email)
    body = response.json()
    logger.info(f"Send OTP response: {body}")
    assert body["success"] is True 
    assert body["code"]==200
    assert body["message"] == "OTP sent successfully"

def test_verify_otp(authorized_api):
    email="shrimalmeet2001@gmail.com"
    otp="123456"
    logger.info(f"Verifying OTP for email: {email} with OTP: {otp}")
    response = authorized_api.verify_otp(email, otp)
    body = response.json()
    logger.info(f"Verify OTP response: {body}")
    assert body["success"]== True
    assert body["code"]==200
    assert body["message"] =="Login successful"
    token = body["results"]["token"]["accessToken"]
    logger.info(f"Retrieved access token: {token}")

    import random
    payload={
        "name":f"new category_{random.randint(1000, 9999)}",
        "category_type":"product"
    }
    logger.info(f"Creating business category with payload: {payload}")
    response = authorized_api.post("/api/v1/business/category/create", json = payload)
    logger.info(f"Create business category response status: {response.status_code}")
    assert response.status_code == 200

def test_create_category(authorized_api):
    payload ={
            "name":"Electronics",
            "category_type": "product"
        }
    logger.info(f"Creating category with payload: {payload}")
    response = authorized_api.post("/api/v1/business/category/create",json=payload)
    logger.info(f"Create category response status: {response.status_code}")
    assert response.status_code==200
