from calculator import CalculatorBase

class TotalDistanceCalculator(CalculatorBase):
	def calculate(self, file_path: str):
		left, right = self.list_generator(file_path)
		
		# sort the lists
		left.sort(), right.sort()
		
		# For example, compute the distance and invert it to obtain a similarity score.
		return sum(abs(x - y) for x, y in zip(left, right))