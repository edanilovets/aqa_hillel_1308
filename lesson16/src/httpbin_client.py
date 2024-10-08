from abc import ABC, abstractmethod
import requests

class ApiClient(ABC):
    BASE_URL = "https://httpbin.org"

    @abstractmethod
    def get(self, endpoint, params=None):
        pass

    @abstractmethod
    def post(self, endpoint, data=None):
        pass

    # TODO: add other methods


class HttpBinApiClient(ApiClient):

    def get(self, endpoint, params=None):
        response = requests.get(f"{self.BASE_URL}{endpoint}", params=params)
        return response

    def post(self, endpoint, data=None):
        response = requests.post(f"{self.BASE_URL}{endpoint}", json=data)
        return response

class HttpBinAuthApiClient(ApiClient):
    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def get(self, endpoint, params=None):
        response = requests.get(f"{self.BASE_URL}{endpoint}", params=params, headers=self.headers)
        return response

    def post(self, endpoint, data=None):
        response = requests.post(f"{self.BASE_URL}{endpoint}", json=data, headers=self.headers)
        return response