from typing import Callable, List

ListGeneratorStrategy = Callable[[List[int], List[int]], float]
from helpers import create_lists_from_file_v2

class CalculatorBase:
    def __init__(self, list_generator: ListGeneratorStrategy = create_lists_from_file_v2):
        """
        Initialize a calculator with a strategy.

        :param strategy: A function that calculates a score given two lists of integers.
        """
        self.list_generator = list_generator
    
    def generate_list(self, file_path: str) -> tuple[List[int], List[int]]:
        """
        Based method for generating a list from a file_path. Should be ubiquitous across calculators.
        """
        return self.list_generator(file_path)
    
    def calculate(self, list1: List[int], list2: List[int]) -> float:
        """
        Abstract method to calculate the score based on the lists.
        Subclasses should implement this method.
        """
        raise NotImplementedError()