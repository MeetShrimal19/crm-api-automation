import pytest
from api.auth_api import AuthAPI

@pytest.fixture
def auth_api():
    base_url ="https://dev-api.profitmanager.in"
    return AuthAPI(base_url)

@pytest.fixture
def auth_token(auth_api):
    email ="shrimalmeet2001@gmail.com"
    otp="123456"

    auth_api.send_otp(email)
    response = auth_api.verify_otp(email, otp)
    body = response.json()

    return body["results"]["token"]["accessToken"]