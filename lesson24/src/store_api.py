from lesson24.src.base_client import BaseClient


class StoreApi(BaseClient):

    def get_inventory(self):
        url = f"/store/inventory"
        response = self._make_request("GET", url)
        return response.json()