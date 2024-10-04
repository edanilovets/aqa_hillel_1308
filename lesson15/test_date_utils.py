from date_utils import DateUtils, DateAssertions


def test_format_date():
    # Arrange
    date_str = "2024-09-29"
    # Act
    formatted_date = DateUtils.format_date(date_str, "%Y-%m-%d", "%m/%d/%Y")
    # Assert
    assert formatted_date == "09/29/2024"

def test_validate_date():
    # Arrange
    # valid_date = get_date_from_ui()
    valid_date = "2024-09-29"
    invalid_date = "29-2024-09"
    # Assert
    assert DateAssertions.validate_date(valid_date) is True
    assert DateAssertions.validate_date(invalid_date) is False

def test_set_timezone():
    DateUtils.set_base_timezone("America/New_York")
    assert DateUtils.get_base_timezone() == "America/New_York"