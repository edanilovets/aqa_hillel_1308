import pytest
from assertpy import assert_that

from lesson24.data.add_pet import pet_data_list
from lesson24.src.app import App



class TestAddPetWithFixtures:

    @pytest.fixture(scope="class", autouse=True)
    def test_setup_teardown(self, app: App):
        app.logger.info("[Setup]...")
        yield
        app.logger.info("[Teardown]...")

    @pytest.fixture(scope="class", params=[
        {
            "id": 201,
            "name": "Fluffy",
            "category": {"id": 1, "name": "Cats"},
            "photoUrls": ["https://example.com/cat1.jpg"],
            "tags": [{"id": 1, "name": "cute"}],
            "status": "available"
        },
        {
            "id": 202,
            "name": "Barky",
            "category": {"id": 2, "name": "Dogs"},
            "photoUrls": ["https://example.com/dog1.jpg"],
            "tags": [{"id": 2, "name": "friendly"}],
            "status": "available"
        }
    ])
    def param_add_pet_data(self, request):
        return request.param

    def test_create_pet_successful_scenario_ID_111(self, app: App, param_add_pet_data):
        response = app.pet.add_pet(param_add_pet_data)
        assert_that(response).is_equal_to(param_add_pet_data)

    def test_create_pet_successful_ID_111(self, app: App, param_add_pet_data):
        response = app.pet.add_pet(param_add_pet_data)
        assert_that(response).is_equal_to(param_add_pet_data)