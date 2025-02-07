from calculator import CalculatorBase
from typing import List

class SimilarityScoreCalculator(CalculatorBase):
    """
    Calculates the similarity by summating the total matching numbers weighted by their values.
    [1 2
     1 1]

    gets a score of 2. (1 (left val) * 1 (instance in the right list)) + (left val) * 1 (instance in the right list))
    """
    def calculate(self, list1: List[int], list2: List[int]) -> float:
        list1.sort()
        list2.sort()

        r = 0
        total, prevAmount = 0, 0
        for l in range(len(list1)):
            if l > 0 and list1[l] == list1[l - 1]:
                total += prevAmount
                continue

            while r < len(list2) and list1[l] > list2[r]:
                r += 1
            
            count = 0
            while r < len(list2) and list1[l] == list2[r]:
                count += 1
                r += 1

            prevAmount = list1[l] * count
            total += prevAmount
        return total