from abc import abstractmethod, ABC
from typing import Generator, List, Optional

class SafetyLevelCheckerBase(ABC):
    
    ### Loading Logic
    def __load_lists(self, file_path: str) -> List[List[int]]:
        try:
            arrays = []
            with open(file_path, 'r') as file:
                for line in file:
                    try:
                        arrays.append([int(num) for num in line.split(' ')])
                    except ValueError:
                        print(f"Line could not be parsed: {line}")
                        continue
            return arrays
        except FileNotFoundError:
            print(f"There was an issue loading your file. {file_path}")
            return []
    
    def get_safe_lines_from_file(self, file_path: str) -> List[List[int]]:
        """Processes a file and returns only the safe lines."""
        return [line for line in self.__load_lists(file_path) if self._is_safe_line(line)]

    ### Safety Checking Methods
    @abstractmethod
    def _is_safe_line(self, line: List[int]) -> Optional[List[int]]:
        """Abstract method: Must be implemented by subclasses to determine if a line is safe."""
        pass

    def _check_safety(self, line: List[int]) -> bool:
        """Checks if a line maintains a consistent direction with valid consecutive differences."""
        if len(line) < 2:
            return True
        direction = line[1] - line[0]
        return all(self._is_safe_pair(a, b, direction) for a, b in self._get_consecutive_pairs(line))

    def _is_safe_pair(self, prev: int, next_: int, direction: int) -> bool:
        """Checks if a pair of numbers follows safety rules (consistent direction & small difference)."""
        return (
            1 <= abs(next_ - prev) <= 3 and  # Difference constraint (≤3)
            ((next_ - prev > 0) == (direction > 0))  # Direction consistency
        )

    ### Utility Methods for Safety Calculations
    def _get_consecutive_pairs(self, line: List[int]) -> List[tuple]:
        """Generates consecutive number pairs from a list."""
        # ex. list = [1, 2, 3] return [(1, 2), (2, 3)]
        return list(zip(line, line[1:]))

    def _get_possible_lines_from_line(self, line: List[int]) -> List[List[int]]:
        """Generates all possible variations of a line with one element removed."""
         # ex. list = [1, 2, 3] return [[1, 2], [2, 3], [1, 3]]
        return [line[:i] + line[i+1:] for i in range(len(line))]