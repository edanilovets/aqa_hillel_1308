import pytest

from lesson24.src.app import App


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa", help="Env to run test against (qa, prod)")
    parser.addoption("--test-id", action="store", default=1, help="Some test id")

# @pytest.fixture(scope="session")
# def database():
#     db = DbConnection()
#     yield db
#     db.close()

@pytest.fixture(scope="module")
def app(request):
    env = request.config.getoption("--env")
    return App(env=env)


@pytest.fixture(scope="module")
def app_auth(request):
    env = request.config.getoption("--env")
    return App(env=env, api_key="special-key")
