from pathlib import Path
import pytest

test_files_dir = Path("../data").absolute()

@pytest.mark.parametrize("test_file", test_files_dir.glob("test_data_*.txt"))
def test_data_management_parametrized(test_file):
    data = test_file.read_text()
    assert "data 1" in data