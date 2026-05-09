import pytest
from api.auth_api import AuthAPI
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture(scope="session")
def auth_api():
    base_url = os.getenv("BASE_URL")
    return AuthAPI(base_url)

@pytest.fixture(scope="session")
def auth_token(auth_api):
    email = os.getenv("EMAIL")
    otp = os.getenv("OTP")

    auth_api.send_otp(email)
    response = auth_api.verify_otp(email, otp)

    assert response.status_code == 200

    body = response.json()
    assert body["success"] is True

    return body["results"]["token"]["accessToken"]

@pytest.fixture
def authorized_api(auth_api, auth_token):
    auth_api.set_token(auth_token)
    yield auth_api
    auth_api.session.headers.pop("Authorization", None) 