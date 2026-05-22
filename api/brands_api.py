from api.base_api import BaseAPI
class BrandsAPI(BaseAPI):
    def get_brand_list(self):
        endpoint = "/api/v1/super-admin/landing/brand/detail"
        return self.get(endpoint)

    def post_brand(self, name, )