class Assertions:

    @staticmethod
    def validate_response_contains(api_response, key: str):
        assert key in api_response, \
            f"Expected {key} in the response {str(api_response)}"


    @staticmethod
    def validate_status_code(api_response, status_code):
        assert api_response.status_code == status_code, \
            f"Expected code {status_code} but was {api_response.status_code}"