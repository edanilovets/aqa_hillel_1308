from pytest import fixture

from lesson17.src.class_auto import Auto

@fixture
def default_auto():
    return Auto(tank=50, fuel_consumption=5)
