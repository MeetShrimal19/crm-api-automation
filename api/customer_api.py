from api.base_api import BaseAPI
class CustomerAPI(BaseAPI):
    
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
