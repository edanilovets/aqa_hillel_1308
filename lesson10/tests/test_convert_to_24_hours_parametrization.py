from pytest import mark

from lesson10.src.functions import convert_to_24_hour


# def test_convert_to_24_hours_am():
#     # Arrange
#     input_time = "02:30 AM"
#     expected_formatted_time = "02:30"
#     # Act
#     result = convert_to_24_hour(input_time)
#     # Assert
#     assert result == expected_formatted_time, \
#         f"Expected {expected_formatted_time}, but got {result}"
#
# def test_convert_to_24_hours_pm():
#     # Arrange
#     input_time = "02:30 PM"
#     expected_formatted_time = "14:30"
#     # Act
#     result = convert_to_24_hour(input_time)
#     # Assert
#     assert result == expected_formatted_time, \
#         f"Expected {expected_formatted_time}, but got {result}"
#
# def test_convert_to_24_hours_noon():
#     # Arrange
#     input_time = "12:00 PM"
#     expected_formatted_time = "00:00"
#     # Act
#     result = convert_to_24_hour(input_time)
#     # Assert
#     assert result == expected_formatted_time, \
#         f"Expected {expected_formatted_time}, but got {result}"
#
# def test_convert_to_24_hours_midnight():
#     # Arrange
#     input_time = "12:00 AM"
#     expected_formatted_time = "12:00"
#     # Act
#     result = convert_to_24_hour(input_time)
#     # Assert
#     assert result == expected_formatted_time, \
#         f"Expected {expected_formatted_time}, but got {result}"

@mark.parametrize("input_time, expected_formatted_time", [
    ("02:30 AM", "02:30"),
    ("02:30 PM", "14:30"),
    ("12:00 PM", "00:00"),
    ("12:00 AM", "12:00"),
])
def test_convert_to_24_hours_params_1(input_time, expected_formatted_time):
    # Act
    result = convert_to_24_hour(input_time)
    # Assert
    assert result == expected_formatted_time, \
        f"Expected {expected_formatted_time}, but got {result}"

def get_input_data():
    return "02:30 AM", "02:30", "02:30 PM", "14:30"

@mark.parametrize("input_time", get_input_data())
def test_convert_to_24_hours_params_2(input_time):
    expected_formatted_time = "XX:XX"
    # Act
    result = convert_to_24_hour(input_time)
    # Assert
    assert result == expected_formatted_time, \
        f"Expected {expected_formatted_time}, but got {result}"