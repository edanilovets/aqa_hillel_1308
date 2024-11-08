import pytest
from assertpy import assert_that, soft_assertions

from lesson24.src.app import App
from lesson24.data.add_pet import pet_data_list


class TestAddPetSoft:
    @pytest.mark.parametrize("pet_data", pet_data_list)
    def test_create_pet_soft(self, app: App, pet_data):
        response = app.pet.add_pet(pet_data)
        with soft_assertions():
            assert_that(response).is_equal_to(pet_data_list[1])
            assert_that(response).is_equal_to(pet_data)
