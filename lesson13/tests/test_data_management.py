from pathlib import Path

def read_test_data(file_name):
    test_data_path = Path("../data") / file_name
    test_data_path = test_data_path.absolute()
    if test_data_path.exists() and test_data_path.is_file():
        return test_data_path.read_text()

def test_data_management():
    data = read_test_data("some_data.txt")
    assert "John1" in data