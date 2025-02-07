import pytest
from total_distance_calculator import TotalDistanceCalculator
from similarity_score_calculator import SimilarityScoreCalculator

@pytest.fixture(scope="class")
def total_distance_calculator() -> TotalDistanceCalculator:
    """
    Fixture that creates a Part1 instance to be shared by tests.
    """
    return TotalDistanceCalculator() # uses the default list creator

@pytest.fixture(scope="class")
def similarity_score_calculator() -> SimilarityScoreCalculator:
    """
    Fixture that creates a Part1 instance to be shared by tests.
    """
    return SimilarityScoreCalculator() # uses the default list creator

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

    def test_d01_p01_good_data(self, dummy_file_factory, total_distance_calculator):
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
        list1, list2 = total_distance_calculator.generate_list(file_path)
        result = total_distance_calculator.calculate(list1, list2)
        assert result == EXPECTED_DISTANCE

    def test_d01_p01_trailing_whitespace(self, dummy_file_factory, total_distance_calculator):
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
        EXPECTED_DISTANCE = 11
        file_path = dummy_file_factory(trailing_whitespace_data)
        list1, list2 = total_distance_calculator.generate_list(file_path)
        result = total_distance_calculator.calculate(list1, list2)
        assert result == EXPECTED_DISTANCE

    def test_d01_p02_good_data(self, dummy_file_factory, similarity_score_calculator):
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
        EXPECTED_DISTANCE = 31
        file_path = dummy_file_factory(trailing_whitespace_data)
        list1, list2 = similarity_score_calculator.generate_list(file_path)
        result = similarity_score_calculator.calculate(list1, list2)
        assert result == EXPECTED_DISTANCE

