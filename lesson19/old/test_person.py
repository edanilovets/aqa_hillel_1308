import pytest
from datetime import datetime

from lesson19.src.clients.swapi_client import SwapiClient

client = SwapiClient()

class TestPerson:
    """Person tests"""

    # bad design
    def test_person_object(self):
        expected_response = {
            "birth_year": "19BBY",
            "eye_color": "blue",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/6/"
            ],
            "gender": "male",
            "hair_color": "blond",
            "height": "172",
            "homeworld": "https://swapi.dev/api/planets/1/",
            "mass": "77",
            "name": "Luke Skywalker",
            "skin_color": "fair",
            "species": [],
            "starships": [
                "https://swapi.dev/api/starships/12/",
                "https://swapi.dev/api/starships/22/"
            ],
            "url": "https://swapi.dev/api/people/1/",
            "vehicles": [
                "https://swapi.dev/api/vehicles/14/",
                "https://swapi.dev/api/vehicles/30/"
            ]
        }
        person = client.get_person(1)
        actual_data = {key: person[key] for key in expected_response}
        assert actual_data == expected_response, f"Mismatch for person with ID 1"

    def test_person_object_additional_fields(self):
        additional_fields = ["created", "edited"]
        person = client.get_person(1)
        for key in additional_fields:
            assert key in person, f"Missing key: {key}"
            try:
                datetime.fromisoformat(person[key].replace("Z", "+00:00"))
            except ValueError:
                pytest.fail(f"Invalid date format for '{key}' key")