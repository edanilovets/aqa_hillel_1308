import pytest
import requests
from pytest import mark, fixture
from datetime import datetime
import logging

PERSON_ID_1 = 1
PERSON_ID_2 = 2

class TestPerson:
    """Person tests"""

    @fixture(scope="class")
    def people_data(self, swapi_client):
        logging.info("People data is fetching...")
        data = {
            PERSON_ID_1: swapi_client.get_person(PERSON_ID_1),
            PERSON_ID_2: swapi_client.get_person(PERSON_ID_2)
        }
        logging.info("People data were fetched successfully!")
        return data

    def test_person_schema(self):
        pass

    @mark.parametrize("person_id,expected_name", [
        (PERSON_ID_1, "Luke Skywalker"),
        (PERSON_ID_2, "C-3PO")
    ])
    def test_person_name(self, people_data, swapi_client, person_id, expected_name):
        person = people_data[person_id]
        assert person["name"] == expected_name, f"Expected name {expected_name}, but got {person['name']}"

    # TODO:
    # def test_hair_color
    # ....

    @mark.parametrize("person_id,expected_number_of_films", [
        (PERSON_ID_1, 4),
        (PERSON_ID_2, 6)
    ])
    def test_person_films(self, people_data, swapi_client, person_id, expected_number_of_films):
        person = people_data[person_id]
        films = person["films"]
        # PersonAssertions.verify_films_length()
        # PersonAssertions.verify_that_links_are_valid()
        assert len(films) == expected_number_of_films, \
            f"Expected films count {expected_number_of_films}, but got {films}"
        for film_urls in films:
            response = requests.get(film_urls)
            assert response.status_code == 200
            film_data = response.json()
            required_film_keys = ["title", "opening_crawl"]
            assert all(key in film_data for key in required_film_keys)

    # TODO:
    # def test_starships
    # ...
    @mark.parametrize("person_id", [
        PERSON_ID_1,
        PERSON_ID_2
    ])
    def test_person_object_additional_fields(self, people_data, swapi_client, person_id):
        additional_fields = ["created", "edited"]
        person = people_data[person_id]
        for key in additional_fields:
            assert key in person, f"Missing key: {key}"
            try:
                datetime.fromisoformat(person[key].replace("Z", "+00:00"))
            except ValueError:
                pytest.fail(f"Invalid date format for '{key}' key")