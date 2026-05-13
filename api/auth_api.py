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

    def get_purchase_by_id(self, purchaseId):
        endpoint = "/api/v1/business/purchase/getByID"
        params={
            "purchaseId": purchaseId
        }
        return self.get(endpoint, params=params)

    def put_purchase(self, purchaseId, payload):
        endpoint="/api/v1/business/purchase/update"
        return self.put(endpoint, json=payload)

    def delete_purchase(self, purchaseId):
        endpoint = "/api/v1/business/purchase/delete"
        params={
            "purchaseId": purchaseId
        }
        return self.delete(endpoint, params=params)


    def post_customers(self, name, area, contact_number):
        endpoint = "/api/v1/business/customer/create"
        payload ={
            "name": name,
            "area": area,
            "contact_number": contact_number
        }
        return self.post(endpoint, json=payload)

    def all_customer_info(self, page=1, limit=10, search=None, customer_name=None, area=None, min_outstanding=None, max_outstanding=None, sort_by=None, order=None, pending=None):
        endpoint = "/api/v1/business/customer/get-all"
        params= {
            "page": page,
            "limit": limit,
            "search": search,
            "customer_name": customer_name,
            "area": area,
            "min_outstanding" : min_outstanding,
            "max_outstanding": max_outstanding,
            "sort_by": sort_by,
            "order" : order,
            "pending" : pending
        }
        return self.get(endpoint, params= params)

    def update_customers(self, customerId, name, area, contact_number):
        endpoint="/api/v1/business/customer/edit"
        params={
            "customerId": customerId
        }
        payload={
             "name": "Updated Name",
             "area": "Uptown",
             "contact_number": "9876543210"
        }
        return self.put(endpoint,params=params, json=payload)

    def delete_customer(self, customer_id):
        endpoint="/api/v1/business/customer/delete"
        params={
            "customerId":customer_id
        }
        return self.delete(endpoint,params=params)

    def add_contact(self, name, email, mobile_code, phone_number, message):
        endpoint = "/api/v1/super-admin/landing/contact"
        payload ={
            "name": name,
            "email": email,
            "mobile_code":mobile_code,
            "phone_number": phone_number,
            "message": message
        }
        return self.post(endpoint, json=payload)

    def get_all_contacts(self, page, limit, search = None, sort_by=None, sort_order=None, type = None, status = None):
        endpoint = "/api/v1/super-admin/landing/contact/inquiries"

        params ={
            "page":page,
            "limit": limit
        }
        return self.get(endpoint, params=params)