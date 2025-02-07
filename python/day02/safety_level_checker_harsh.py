from safety_level_checker_base import SafetyLevelCheckerBase
from typing import List

class SafetyLevelCheckerHarsh(SafetyLevelCheckerBase):
    def is_safe_line(self, line: List[int]) -> bool:
        """Determines whether a line is safe given the condition. """
        if len(line) < 2:
            return True # a single number is necessarily a safe one
        
        direction = line[0] > line[1]
        for i in range(1, len(line)):
            safeDir = (line[i-1] > line[i]) == direction
            safeDif = abs(line[i] - line[i-1]) <= 3
            if not (safeDif and safeDir):
                return False
        return True