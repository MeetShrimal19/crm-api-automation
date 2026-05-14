import requests 
from api.base_api import BaseAPI

class AuthAPI(BaseAPI):
    def send_otp(self, email):
        endpoint = "/api/v1/business/auth/login"
        payload={
            "email": email
        }
        return self.post(endpoint, json=payload)
    
    def verify_otp(self, email, otp):
        endpoint = "/api/v1/business/auth/verify-otp"
        payload={
            "email": email,
            "otp": otp 
        }
        return self.post(endpoint, json=payload)
        
