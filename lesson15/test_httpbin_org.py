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

    assert api_response == 200
    assert "url" in api_response
    assert len(api_response) == 4

def test_get_data1():
    url = f"{BASE_URL}/get"

    response = requests.get(url)
    api_response = ApiResponse(response)

    assert api_response == 201
    assert "url" in api_response
    assert len(api_response) == 4
