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
            "otp": "123456" 
        }
        return self.post(endpoint, json=payload)
        
    def get_materials(self, page =1, limit = 5, search = None, category_type = None, headers = None):
        endpoint = "/api/v1/business/material/get"
        params={
            "page": page,
            "limit": limit,
            "search": search,
            "category_type": category_type
        }

        if search:
            params["search"] = search 

        if category_type:
            params["category_type"]=category_type
        return self.get(endpoint, headers=headers, params = params)

    def get_supplier(self, page =1, limit =5 , headers=None, search = None):
        endpoint="/api/v1/business/supplier/get"
        params={
            "page":page,
            "limit": limit,
            "search": search

        }

        if search:
            params["search"]= search
        return self.get(endpoint, headers= headers, params= params)