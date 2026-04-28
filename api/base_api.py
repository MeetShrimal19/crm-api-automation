import requests 
class BaseAPI:

    def __init__(self, base_url):
        self.base_url = base_url
    
    def get(self, endpoint, headers=None, params = None):
        return requests.get(f"{self.base_url}{endpoint}", headers = headers, params=params)
    
    def post(self, endpoint, json=None, headers=None):
        return requests.post(f"{self.base_url}{endpoint}", json=json, headers=headers)
    
    def put(self, endpoint, headers=None, json= None, params=None):
        return requests.put(f"{self.base_url}{endpoint}", json=json, headers=headers, params=params)
    
    def delete(self, endpoint, headers=None, params= None):
        return requests.delete(f"{self.base_url}{endpoint}", headers=headers, params=params)