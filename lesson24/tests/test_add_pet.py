import pytest
from assertpy import assert_that

from lesson24.data.add_pet import pet_data_list
from lesson24.src.app import App


@pytest.mark.parametrize("pet_data", pet_data_list)
def test_create_pet_successful_scenario(app: App, pet_data):
    response = app.pet.add_pet(pet_data)
    assert_that(response).is_equal_to(pet_data)
