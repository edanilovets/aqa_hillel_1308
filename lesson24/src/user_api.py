from lesson24.src.base_client import BaseClient


class UserApi(BaseClient):

    def get_user_by_name(self, username: str):
        url = f"/user/{username}"
        response = self._make_request("GET", url)
        return response.json()