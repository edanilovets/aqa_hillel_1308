import pytest
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from lesson19.data.people.people_schema import response_schema


class TestAllPeople:

    @pytest.mark.parametrize("page", [1, 2, 3])  # first, middle, last page
    def test_all_people_schema(self, page, swapi_client):
        response_json = swapi_client.get_all_people(params={"page": page})

        try:
            validate(response_json, schema=response_schema)
        except ValidationError:
            pytest.fail("Schema is not valid")

    # can be refactored to use @dataclass
    def test_get_all_people(self, swapi_client):
        response_json = swapi_client.get_all_people()
        assert isinstance(response_json, dict)
        assert isinstance(response_json['results'], list)
        assert isinstance(response_json['count'], int)
        assert isinstance(response_json['next'], str)
        assert response_json['previous'] is None
        assert response_json['count'] == 82

        for person in response_json['results']:
            assert "name" in person
            assert "gender" in person

    # can be parametrized
    def test_next_and_previous_pages(self, swapi_client):
        first_page = swapi_client.get_all_people(params={"page": 2})
        next_url = first_page['next']
        previous_url = first_page['previous']

        if next_url:
            next_page_num = int(next_url.split("=")[-1])
            third_page = swapi_client.get_all_people(params={"page": next_page_num})
            assert isinstance(third_page, dict)
            assert isinstance(third_page['results'], list)
            assert isinstance(third_page['count'], int)
            assert isinstance(third_page['next'], str)
            assert third_page['previous'] is not None
            assert third_page['count'] == 82

            for person in third_page['results']:
                assert "name" in person
                assert "gender" in person

        if previous_url:
            previous_page_num = int(previous_url.split("=")[-1])
            first_page = swapi_client.get_all_people(params={"page": previous_page_num})
            assert isinstance(first_page, dict)
            assert isinstance(first_page['results'], list)
            assert isinstance(first_page['count'], int)
            assert isinstance(first_page['next'], str)
            assert first_page['previous'] is None
            assert first_page['count'] == 82

            for person in first_page['results']:
                assert "name" in person
                assert "gender" in person