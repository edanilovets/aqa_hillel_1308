"""
Список містить словники - дані співробітників фірми (прізвище, зарплата і стать).
Скласти функцію, яка повертає тапл:
а) прізвище особи, яка має найбільшу зарплату (якщо більше одного - перше по алфавіту);
б) розмір найменшої зарплати чоловіків,
в) розмір найвищої зарплати жінок
[
    {"name": "Azimova", "salary": 20000, "gender": "f"},
    {"name": "Borenko", "salary": 9000, "gender": "m"},
    {"name": "Vasilenko", "salary": 10000, "gender": "m"},
    {"name": "Zabolotna", "salary": 25000, "gender": "f"},
    {"name": "Koval", "salary": 35000, "gender": "m"},
    {"name": "Koval", "salary": 35000, "gender": "m"},
]
"""
import pytest

from data.data_test_demo import some_dict

def get_salaries_information(some_dict):
    # а) прізвище особи, яка має найбільшу зарплату (якщо більше одного - перше по алфавіту);
    max_salary_name = some_dict[0]["name"]
    max_salary = some_dict[0]["salary"]

    for i in some_dict:
        if i["salary"] > max_salary:  # TypeError
            max_salary = i["salary"]
            max_salary_name = i["name"]
        elif i["salary"] == max_salary:
            if i["name"] < max_salary_name:
                max_salary_name = i["name"]
    return max_salary_name

def test_salaries_information1():
    # Arrange
    some_dict = {

    }
    # Act
    with pytest.raises(TypeError) as exc_info:
        get_salaries_information(some_dict)
    data = str(exc_info.value)
    assert data == None

def test_salaries_information3():
    with pytest.raises(TypeError) as exc_info:
        get_salaries_information(some_dict)
    data = str(exc_info.value)
    assert data == None

def test_salaries_information2():
    with pytest.raises(TypeError) as exc_info:
        get_salaries_information(some_dict)
    data = str(exc_info.value)
    assert data == None
