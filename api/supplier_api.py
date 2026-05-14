from api.base_api import BaseAPI
class SupplierAPI(BaseAPI):
    
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

