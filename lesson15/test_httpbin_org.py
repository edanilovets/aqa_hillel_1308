import requests


class ApiResponse:

    def __init__(self, response):
        self.status_code = response.status_code
        self.json_data = response.json()

    def __eq__(self, other):
        return self.status_code == other

    def __contains__(self, item):
        return item in self.json_data

    def __len__(self):
        return len(self.json_data)


BASE_URL = "https://httpbin.org"

def test_get_data():
    url = f"{BASE_URL}/get"

    response = requests.get(url)
    api_response = ApiResponse(response)

    # Assertions using dunder methods
    assert api_response.status_code == 200, f"Expected status code 200, but got {api_response.status_code}"
    assert "url" in api_response, "Expected 'url' in the response"
    assert len(api_response) > 1, "Expected more than 1 field in the response"

def test_create_data():
    url = f"{BASE_URL}/post"
    data = {"name": "John Doe", "email": "john@example.com"}

    response = requests.post(url, json=data)
    api_response = ApiResponse(response)

    # Assertions using dunder methods
    assert api_response.status_code == 200, f"Expected status code 200, but got {api_response.status_code}"
    assert "json" in api_response, "Expected 'json' in the response"
    assert len(api_response.json_data['json']) == 2, "Expected exactly 2 fields in the response JSON"
