from calculator import CalculatorBase
from typing import List

class TotalDistanceCalculator(CalculatorBase):
	"""
	This is a subclass that calculates by summing the distance between closest nodes. It gurantees closeness by sorting.
	"""
	def calculate(self, list1: List[int], list2: List[int]) -> float:
		list1.sort()
		list2.sort()
		
		# For example, compute the distance and invert it to obtain a similarity score.
		return sum(abs(x - y) for x, y in zip(list1, list2))