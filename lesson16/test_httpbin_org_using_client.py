import requests
from src.httpbin_client import HttpBinApiClient, HttpBinAuthApiClient


class TestHTTPMethods:

    client = HttpBinApiClient()
    auth_client = HttpBinAuthApiClient("adadfawdankjwadnkjand")

    def test_get_data(self):
        response = self.client.get("/get")
        response = self.auth_client.get("/get")
        assert response.status_code == 200

    def test_create_data(self):
        data = {"name": "John Doe", "email": "john@example.com"}
        response = self.client.post("/post", data=data)
        assert response.status_code == 200
