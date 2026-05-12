def test_send_otp(authorized_api):
    email="shrimalmeet2001@gmail.com"
    response = authorized_api.send_otp(email)
    print(response.json())
    body = response.json()
    assert body["success"] is True 
    assert body["code"]==200
    assert body["message"] == "OTP sent successfully"

def test_verify_otp(authorized_api):
    email="shrimalmeet2001@gmail.com"
    otp="123456"
    response = authorized_api.verify_otp(email, otp)
    body = response.json()
    assert body["success"]== True
    assert body["code"]==200
    assert body["message"] =="Login successful"
    token = body["results"]["token"]["accessToken"]

    import random
    payload={
        "name":f"new category_{random.randint(1000, 9999)}",
        "category_type":"product"
    }

    response = authorized_api.post("/api/v1/business/category/create", json = payload)
    assert response.status_code == 200

    print("Token:", token)

def test_create_category(authorized_api):
    
    payload ={
            "name":"Electronics",
            "category_type": "product"
        }

    response = authorized_api.post("/api/v1/business/category/create",json=payload)
    assert response.status_code==200
