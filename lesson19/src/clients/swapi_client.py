import requests
from lesson19.src.clients.base_client import BaseClient
import logging

class SwapiClient(BaseClient):
    """API Client for SWAPI."""

    BASE_URL = "https://swapi.dev/api"

    def get_person(self, person_id: int) -> dict:
        """Retrieves a person by id"""
        logging.info(f"Getting person with ID={person_id}")
        url = f"{self.BASE_URL}//people/{person_id}/"
        response = self.make_request("GET", url)
        return response.json()

    def get_all_people(self, params=None) -> dict:
        """Retrieves all people"""
        logging.info(f"Getting all people")
        url = f"{self.BASE_URL}/people/"
        response = self.make_request("GET", url, params=params)
        return response.json()

    # TODO: