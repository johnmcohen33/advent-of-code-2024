from safety_level_checker_base import SafetyLevelCheckerBase
from typing import List, Optional
import math

class SafetyLevelCheckerHarsh(SafetyLevelCheckerBase):    
    def is_safe_line(self, line: List[int]) -> Optional[List[int]]:
        if len(line) < 2:
            return line
        dir = line[1] - line[0]
        pairs = self._get_consecutive_pairs(line)  # Get consecutive pairs
        return line if all(self._are_nums_safe_helper(a, b, dir) for a, b in pairs) else None