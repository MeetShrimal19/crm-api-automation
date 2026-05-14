from api.base_api import BaseAPI
class ContactAPI(BaseAPI):
        


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
