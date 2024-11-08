import logging

import pytest
from assertpy import assert_that

from lesson24.src.app import App
from lesson24.data.add_pet import pet_data_list


class TestAddPetBuiltInFixtures:
    @pytest.fixture(scope="class")
    def test_setup_teardown(self, app: App):
        app.logger.info("[Setup]...")
        yield
        app.logger.info("[Teardown]...")


    @pytest.mark.parametrize("pet_data", pet_data_list)
    def test_create_pet_successful_scenario3(self, app: App, pet_data):
        response = app.pet.add_pet(pet_data)
        assert_that(response).is_equal_to(pet_data)

    # tmpdir example
    def test_get_pet_tmpdir(self, app: App, tmpdir):
        invalid_pet_id = None
        log_file = tmpdir.join("temp_log.txt")
        app.logger.addHandler(logging.FileHandler(log_file))
        with pytest.raises(RuntimeError) as e:
            app.pet.get_pet_by_id(invalid_pet_id)
        assert_that(str(e.value)).contains("404")
        file_contents = log_file.read()
        assert_that(file_contents).contains("404")

    def test_get_pet_caplog(self, app: App, caplog, request):
        pet_id = 201

        with caplog.at_level(logging.INFO):
            app.logger.info(f"Running test {request.node.name}...")
            app.pet.get_pet_by_id(pet_id)
        assert_that(caplog.text).contains(f"Running test {request.node.name}")
        assert_that(caplog.text).contains("INFO Making")

    def test_get_pet_zero_id_monkeypatch(self, app: App, monkeypatch, request):
        # E2E tests
        # Step1: Request 1
        def mock_get_pet_by_id(pet_id: int):
            if pet_id == 0:
                raise RuntimeError("404 Not found")

        monkeypatch.setattr(app.pet, "get_pet_by_id", mock_get_pet_by_id)
        with pytest.raises(RuntimeError) as e:
            app.pet.get_pet_by_id(0)
        assert_that(str(e.value)).contains("404")

        # Step 2: Request 2
        # Step 3: Request 3

    def test_get_pet_long_id_monkeypatch(self, app: App, monkeypatch):
        # E2E tests
        # Step1: Request 1
        def mock_get_pet_by_id(pet_id: int):
            if pet_id == 12345:
                return {
                    "id": 12345,
                    "category": {
                        "id": 0,
                        "name": "string"
                    },
                    "name": "doggie",
                    "photoUrls": [
                        "string"
                    ],
                    "tags": [
                        {
                            "id": 0,
                            "name": "string"
                        }
                    ],
                    "status": "available"
                }

        monkeypatch.setattr(app.pet, "get_pet_by_id", mock_get_pet_by_id)
        pet_data = app.pet.get_pet_by_id(12345)

        # Step 2: Request 2
        response = app.pet.add_pet(pet_data)
        assert_that(response).is_equal_to(response)

        # Step 3: Request 3

    # works only on prod
    @pytest.mark.usefixtures("test_setup_teardown")
    def test_get_pet_pytestconfig(self, app: App, pytestconfig):
        test_id = pytestconfig.getoption("--test-id")
        pet_data = app.pet.get_pet_by_id(test_id)
        assert_that(pet_data["id"]).is_equal_to(str(test_id))