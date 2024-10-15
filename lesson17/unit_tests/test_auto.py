import pytest
from pytest import mark

from lesson17.src.class_auto import Auto

#########################################
# Test class initialization (positive)

# bad test design
def test_auto_initialization():
    car = Auto(tank=50, fuel_consumption=5)
    assert car.tank == 50
    assert car.fuel_consumption == 5
    assert car.engine_is_on is False   # None, False, True;  == --> is
    assert car.current_level_of_fuel == 50

# Test class initialization (positive) parametrized
@mark.parametrize("tank,fuel_consumption,attribute,expected_value", [
    (50, 5, "tank", 50),
    (50, 5, "fuel_consumption", 5),
    (50, 5, "engine_is_on", False),
    (50, 5, "current_level_of_fuel", 50),
    (35.4, 5.3, "tank", 35.4),
    (50.09, 10.11, "fuel_consumption", 10.11),
])
def test_auto_initialization_params(tank, fuel_consumption, attribute, expected_value):
    car = Auto(tank=tank, fuel_consumption=fuel_consumption)
    actual_value = getattr(car, attribute)
    assert actual_value == expected_value

#########################################
# Test methods
# USE FIXTURES
def test_turn_on_engine(default_auto):
    default_auto._turn_on_engine()
    assert default_auto.engine_is_on is True

def test_turn_off_engine(default_auto):
    default_auto._turn_on_engine()
    default_auto._turn_off_engine()
    assert default_auto.engine_is_on is False

def test_start_engine(default_auto):
    default_auto.start()
    assert default_auto.engine_is_on is True

def test_stop_engine(default_auto):
    default_auto._turn_on_engine()
    default_auto.stop()
    assert default_auto.engine_is_on is False

#########################################
# Test class initialization (negative)
def test_invalid_tank():
    with pytest.raises(ValueError):
        Auto(tank=-50, fuel_consumption=5)

    with pytest.raises(ValueError):
        Auto(tank=0, fuel_consumption=5)

def test_invalid_fuel_consumption():
    with pytest.raises(ValueError):
        Auto(tank=50, fuel_consumption=-5)

    with pytest.raises(ValueError):
        Auto(tank=50, fuel_consumption=0)

def test_invalid_type_of_tank():
    with pytest.raises(TypeError):
        Auto(tank="50", fuel_consumption=5)

def test_invalid_type_of_fuel_consumption():
    with pytest.raises(TypeError):
        Auto(tank=True, fuel_consumption=5)
