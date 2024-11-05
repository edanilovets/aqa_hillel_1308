import pytest
import logging

from lesson23.src.petstore_client import PetStoreClient


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa", help="Env to run test against (qa, prod)")

def pytest_configure(config):
    config.option.log_cli_level = 'INFO'

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    file_handler = logging.FileHandler('lesson23/petstore.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    logging.getLogger().addHandler(file_handler)

@pytest.fixture(scope="module")
def petstore_client(request):
    env = request.config.getoption("--env")
    return PetStoreClient(env=env)

@pytest.fixture(scope="module")
def petstore_auth_client(request):
    env = request.config.getoption("--env")
    return PetStoreClient(api_key="special-key", env=env)