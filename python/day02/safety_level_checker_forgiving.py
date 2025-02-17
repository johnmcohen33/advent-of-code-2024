from safety_level_checker_harsh import SafetyLevelCheckerHarsh
from typing import List
import math

class SafetyLevelCheckerForgiving(SafetyLevelCheckerHarsh):
    def _is_safe_line(self, line) -> List[int]:
        """ 
        Returns True if a line is safe.
        A line is safe if:
        - It is safe under SafetyLevelCheckerHarsh's definition.
        - If needed, **removing one number** can make it safe.
        """
        
        if super()._is_safe_line(line):
            return line

        return line if self.__can_be_made_safe(line) else None
    
    def __can_be_made_safe(self, line):
        """
        Is there a variation of this line that could be made safe?
        """
        for possibleLine in self._get_possible_lines_from_line(line):
           if all(self._is_safe_pair(a,b,(possibleLine[1]-possibleLine[0])) for a,b in self._get_consecutive_pairs(possibleLine)):
               return True
        return False