from safety_level_checker_base import SafetyLevelCheckerBase
from typing import List, Optional

class SafetyLevelCheckerHarsh(SafetyLevelCheckerBase):    
    def _is_safe_line(self, line: List[int]) -> Optional[List[int]]:
        """ 
        Returns True if a line is safe.
        A line is safe if:
        - It maintains a consistent direction (always increasing or always decreasing).
        - The difference between consecutive numbers is at most 3.
        """
        if len(line) < 2:
            return line
        return line if self._check_safety(line) else None