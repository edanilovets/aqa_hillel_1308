import requests
from src.assertions import Assertions

class ApiResponse:

    def __init__(self, response: requests.Response):
        self.status_code = response.status_code
        self.json_data = response.json()

    def __eq__(self, other):
        return self.status_code == other

    def __contains__(self, item):
        return item in self.json_data

    def __len__(self):
        return len(self.json_data)

    def __str__(self):
        pass


BASE_URL = "https://httpbin.org"

def test_get_data():
    url = "/get"
    api_response = make_request("GET", url, 200)
    Assertions.validate_response_contains(api_response, "url")
    assert len(api_response) > 1, "Expected more than 1 field in the response"

def test_create_data():
    url = "/post"
    data = {"name": "John Doe", "email": "john@example.com"}
    api_response = make_request("POST", url, 200, json=data)
    Assertions.validate_response_contains(api_response, "json")
    assert len(api_response.json_data['json']) == 2, "Expected exactly 2 fields in the response JSON"

##############################################################
# DRY
##############################################################
def make_request(method, endpoint, expected_status_code, **kwargs):
    url = f"{BASE_URL}{endpoint}"
    response = requests.request(method, url, **kwargs)
    assert response.status_code == expected_status_code, \
        f"Expected status code {expected_status_code}, but was {response.status_code}"
    return ApiResponse(response)