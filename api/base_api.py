import requests 
from utils.logger import get_logger
logger = get_logger()
class BaseAPI:

    def __init__(self, base_url):
        self.base_url = base_url
    
    def get(self, endpoint, headers=None, params = None):
        url = f"{self.base_url}{endpoint}"

        logger.info(f" Get Request -> {url} ")
        logger.info(f"Params -> {params}")

        response = requests.get(url, headers=headers, params=params)

        logger.info(f"Status Code -> {response.status_code}")
        logger.info(f"Response -> {response.text}")

        return response
    
    def post(self, endpoint, json=None, headers=None):
        url = f"{self.base_url}{endpoint}"

        logger.info(f"POST Request -> {url}")
        logger.info(f"Payload -> {json}")

        response = requests.post(url, json=json, headers=headers)

        logger.info(f"Status Code -> {response.status_code}")
        logger.info(f"Response -> {response.text}")

        return response
    
    def put(self, endpoint, headers=None, json=None, params=None):
        url = f"{self.base_url}{endpoint}"

        logger.info(f"PUT Request -> {url}")
        logger.info(f"Payload -> {json}")
        logger.info(f"Params -> {params}")

        response = requests.put(url, json=json, headers=headers, params=params)

        logger.info(f"Status Code -> {response.status_code}")
        logger.info(f"Response -> {response.text}")

        return response
    
    def delete(self, endpoint, headers=None, params=None):
        url = f"{self.base_url}{endpoint}"

        logger.info(f"DELETE Request -> {url}")
        logger.info(f"Params -> {params}")

        response = requests.delete(url, headers=headers, params=params)

        logger.info(f"Status Code -> {response.status_code}")
        logger.info(f"Response -> {response.text}")

        return response