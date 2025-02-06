import pytest
from part1 import Part1

@pytest.fixture(scope="class")
def part1() -> Part1:
    """
    Fixture that creates a Part1 instance to be shared by tests.
    """
    return Part1()

@pytest.fixture
def dummy_file_factory(tmp_path):
    """
    Returns a factory function that creates a temporary file with given dummy data.
    """
    def _create_dummy_file(dummy_data: str) -> str:
        # Create a file named "dummy.txt" in the temporary directory.
        file_path = tmp_path / "dummy.txt"
        file_path.write_text(dummy_data)
        return str(file_path)
    return _create_dummy_file

class TestDay01:

    def test_advent_of_code_day_1_part_1_v1(self, dummy_file_factory, part1):
        """
        Test version 1 of the solution using the dummy file.
        """
        EXPECTED_DISTANCE = 11
        good_data = """\
        3   4
        4   3
        2   5
        1   3
        3   9
        3   3"""
        file_path = dummy_file_factory(good_data)
        result = part1.advent_of_code_day_1_part_1_v1(file_path)
        assert result == EXPECTED_DISTANCE

    def test_advent_of_code_day_1_part_1_v1_trailing_whitespace(self, dummy_file_factory, part1):
        """
        Test version 1 of the solution using the dummy file with trailing whitespace.
        """
        trailing_whitespace_data = """\
        3   4
        4   3
        2   5
        1   3
        3   9
        3   3
        """ # notice the extra indent here.
        file_path = dummy_file_factory(trailing_whitespace_data)
        with pytest.raises(IndexError):
            part1.advent_of_code_day_1_part_1_v1(file_path)