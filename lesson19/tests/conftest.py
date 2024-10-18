from lesson19.src.clients.swapi_client import SwapiClient
from pytest import fixture
import logging

@fixture(scope="module")
def swapi_client():
    logging.info("Creating SWAPI client..")
    return SwapiClient()