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
    
    def update_supplier(self, supplier_id, payload, headers= None):
        endpoint = "/api/v1/business/supplier/update"
        params={
            "supplier_id":supplier_id 
        }
        return self.put(endpoint, json=payload, headers=headers, params=params)
    
    def delete_supplier(self, supplier_id, headers=None):
        endpoint="/api/v1/business/supplier/delete"
        params={
            "supplier_id":supplier_id
        }

        return self.delete(endpoint, headers=headers, params=params)

    def add_purchase(self, supplier_id, product_id, quantity, cost_price, payment_date, payment_status, amount_paid, headers=None):
        endpoint ="/api/v1/business/purchase/add"
        payload ={
            "supplier_id": supplier_id,
            "product_id": product_id,
            "quantity": quantity,
            "cost_price": cost_price,
            "payment_date": payment_date,
            "payment_status": payment_status,
            "amount_paid": amount_paid
            }
        return self.post(endpoint, json=payload, headers=headers)

    def get_purchase(self, page, limit, search=None, headers=None):
        endpoint="/api/v1/business/purchase/get-all"
        params={
            "page":page,
            "limit": limit,
            "search":search
        }

        return self.get(endpoint, headers=headers, params=params)
