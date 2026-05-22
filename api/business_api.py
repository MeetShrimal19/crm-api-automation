from api.base_api import BaseAPI
class BusinessAPI(BaseAPI):
    def create_business_management(self, name, email, address, mobile_code, mobile_number):
        endpoint = "/api/v1/super-admin/business/add"

        payload={
            "name": name,
            "email": email,
            "address": address,
            "mobile_code": mobile_code,
            "mobile_number": mobile_number
        }

        return self.post(endpoint, json=payload)

    def get_business_details(self, page, limit):
        endpoint = "/api/v1/super-admin/business/get-all"
        params={
            "page":page,
            "limit":limit
        }
        return self.get(endpoint,params = params)

    def fetch_business_by_id(self, id):
        endpoint="/api/v1/super-admin/business/get"
        params={
            "id":id
        }
        return self.get(endpoint, params=params)
    
    def update_business_id(self, businessId):
        endpoint="/api/v1/super-admin/business/status"
        params={
            "businessId": businessId
        }
        return self.put(endpoint, params=params)
