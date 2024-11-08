import pytest
from assertpy import assert_that

from lesson23.data.add_pet import pet_data_list
from lesson23.src.petstore_client import PetStoreClient


@pytest.mark.parametrize("pet_data", pet_data_list)
def test_create_pet_successful_scenario(petstore_client: PetStoreClient, pet_data):
    response = petstore_client.add_pet(pet_data)
    assert_that(response).is_equal_to(pet_data)
