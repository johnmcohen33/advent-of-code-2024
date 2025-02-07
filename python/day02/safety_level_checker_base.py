from typing import Generator, List, Optional
import math

class SafetyLevelCheckerBase:
    def __generate_nums_from_file(self, file_path: str) -> Generator[List[int], any, None]:
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    if line.strip():
                        try:
                            yield list(map(int, line.split()))
                        except ValueError as ve:
                            raise ValueError(f"Line could not be parsed into ints: {line}") from ve
        except FileNotFoundError as fe:
            raise FileNotFoundError(f"Error: file not found {file_path}") from fe
    
    def _get_consecutive_pairs(self, line):
        """Returns a list of consecutive pairs from a given list."""
        return list(zip(line, line[1:]))  # Generates [(a, b), (b, c), (c, d), ...]

    def _are_nums_safe_helper(self, prev: int, next: int, diffSign: int) -> bool:
        return (
            1 <= abs(next - prev) <= 3
            and ((next - prev > 0) == (diffSign > 0))
        )
    
    def _get_possible_lines_from_line(self, line: List[int]) -> bool:
        """
        returns all possible combinations of lines from a line
        """
        return [line[:i] + line[i+1:] for i in range(len(line))]
    
    def get_safe_lines_from_file(self, file_path: str) -> List[List[int]]:
        return [result for line in self.__generate_nums_from_file(file_path) 
            if (result := self.is_safe_line(line))]
    
    def is_safe_line(self, line: List[int]) -> Optional[List[int]]:
        """
        Determines if a given line of integers meets the safety criteria.
        This is an abstract method that should be implemented by child classes
        to define specific safety checks.
        Args:
            line (List[int]): A list of integers representing the line to be checked.
        Returns:
            List[int] | None: List of ints if the line is considered safe, False otherwise.
        """
        raise NotImplementedError("Please implement in child classes.")
