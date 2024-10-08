from src.httpbin_client import HttpBinApiClient, HttpBinAuthApiClient
from src.assertions import Assertions

class TestHTTPMethods(Assertions, HttpBinApiClient):

    def test_get_data(self):
        response = self.get("/get")
        assert response.status_code == 200

    def test_create_data(self):
        data = {"name": "John Doe", "email": "john@example.com"}
        response = self.post("/post", data=data)
        assert response.status_code == 200


class TestAuthHTTPMethods(Assertions, HttpBinAuthApiClient):

    def test_get_data(self):
        response = self.get("/get")
        self.validate_status_code(response, 200)

    def test_create_data(self):
        data = {"name": "John Doe", "email": "john@example.com"}
        response = self.post("/post", data=data)
        self.validate_status_code(response, 200)
