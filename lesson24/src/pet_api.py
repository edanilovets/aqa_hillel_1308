from lesson24.src.base_client import BaseClient


class PetApi(BaseClient):

    def get_pet_by_id(self, pet_id: int):
        url = f"/pet/{pet_id}"
        response = self._make_request("GET", url)
        return response.json()

    def add_pet(self, pet_data: dict):
        url = "/pet"
        self.logger.info(f"Adding pet...")
        response = self._make_request("POST", url, json=pet_data)
        return response.json()

    def delete_pet(self, pet_id: int):
        url = f"/pet/{pet_id}"
        response = self._make_request("DELETE", url)
        return response.json()