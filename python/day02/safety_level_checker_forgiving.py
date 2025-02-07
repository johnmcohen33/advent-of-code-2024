from safety_level_checker_base import SafetyLevelCheckerBase
from typing import List
import math

class SafetyLevelCheckerForgiving(SafetyLevelCheckerBase):
    def is_safe_line(self, line) -> List[int]:
        """ 
        Returns True if a line is safe.
        A line is safe if:
        - It maintains a consistent direction (always increasing or always decreasing).
        - The difference between consecutive numbers is at most 3.
        - If needed, **removing one number** can make it safe.
        """
        if len(line) < 2:
            return line

        # First, check if the original line is already safe
        original_pairs = self._get_consecutive_pairs(line)
        if all(self._are_nums_safe_helper(a, b, a - b) for a, b in original_pairs):
            return line

        # If not safe, generate possible lines with one number removed
        possibleLines = self._get_possible_lines_from_line(line)

        for possibleLine in possibleLines:
            pairs = self._get_consecutive_pairs(possibleLine)
            dir = possibleLine[1] - possibleLine[0]  # Determine direction dynamically            
            if all(self._are_nums_safe_helper(a, b, dir) for a, b in pairs):
                return line

        return None