import pytest

from lesson23.src.petstore_client import PetStoreClient
from lesson23.data.add_pet import pet_data_list
from assertpy import assert_that


@pytest.fixture(autouse=True)
def setup(petstore_auth_client: PetStoreClient):
    for pet_data in pet_data_list:
        try:
            petstore_auth_client.delete_pet(pet_data["id"])
        except RuntimeError:
            pass
    yield
    for pet_data in pet_data_list:
        try:
            petstore_auth_client.delete_pet(pet_data["id"])
        except RuntimeError:
            pass


@pytest.mark.parametrize("pet_data", pet_data_list, ids=[f"pet-{pet['id']}" for pet in pet_data_list])
def test_create_and_get_pet(petstore_auth_client: PetStoreClient, pet_data):
    # Step 1: Get pet without id
    with pytest.raises(RuntimeError) as e:
        petstore_auth_client.get_pet_by_id(pet_data["id"])
    # Step 2: Add pet
    response = petstore_auth_client.add_pet(pet_data)
    assert_that(response).is_equal_to(pet_data)
    # Step 3: Get pet by id
    pet_id = pet_data["id"]
    response = petstore_auth_client.get_pet_by_id(pet_id)
    assert_that(response).is_equal_to(pet_data)

