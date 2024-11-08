import pytest

from lesson23.src.petstore_client import PetStoreClient


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa", help="Env to run test against (qa, prod)")


@pytest.fixture(scope="module")
def petstore_client(request):
    env = request.config.getoption("--env")
    return PetStoreClient(env=env)


@pytest.fixture(scope="module")
def petstore_auth_client(request):
    env = request.config.getoption("--env")
    return PetStoreClient(api_key="special-key", env=env)
