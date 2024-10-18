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

