from api.base_api import BaseAPI
class MaterialAPi(BaseAPI):
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
