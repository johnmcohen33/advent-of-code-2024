import pytest
from part1 import Part1


@pytest.fixture(scope="class")
def part1() -> Part1:
    """
    Fixture that creates a Part1 instance to be shared by tests.
    """
    return Part1()

@pytest.fixture
def good_dummy_file(tmp_path):
    """
    Create a temporary dummy file with known input data.
    The tmp_path fixture (provided by pytest) gives a temporary directory.
    """
    # A sample input that matches the problem's description.
    DUMMY_DATA = """\
    3   4
    4   3
    2   5
    1   3
    3   9
    3   3"""

    file_path = tmp_path / "dummy.txt"
    file_path.write_text(DUMMY_DATA)
    return str(file_path)

@pytest.fixture
def trailing_whitespace_dummy_file(tmp_path):
    """
    Create a temporary dummy file with known input data.
    The tmp_path fixture (provided by pytest) gives a temporary directory.
    Has a trailing whitespace at the end.
    """
    DUMMY_DATA = """\
    3   4
    4   3
    2   5
    1   3
    3   9
    3   3
    """

    file_path = tmp_path / "dummy.txt"
    file_path.write_text(DUMMY_DATA)
    return str(file_path)

class TestDay01:

    def test_advent_of_code_day_1_part_1_v1(self, good_dummy_file, part1):
        """
        Test version 1 of the solution using the dummy file.
        """
        EXPECTED_DISTANCE = 11
        result = part1.advent_of_code_day_1_part_1_v1(good_dummy_file)
        assert result == EXPECTED_DISTANCE

    def test_advent_of_code_day_1_part_1_v1_trailing_whitespace(self, trailing_whitespace_dummy_file, part1):
        """
        Test version 1 of the solution using the dummy file with trailing whitespace.
        """
        with pytest.raises(IndexError):
            part1.advent_of_code_day_1_part_1_v1(trailing_whitespace_dummy_file)