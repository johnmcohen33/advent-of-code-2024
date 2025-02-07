from typing import Generator, List

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
    
    def get_safe_lines_from_file(self, file_path: str) -> int:
        return sum(1 for line in self.__generate_nums_from_file(file_path) if self.is_safe_line(line))

    def is_safe_line(self, line: List[int]) -> bool:
        """
        Determines if a given line of integers meets the safety criteria.
        This is an abstract method that should be implemented by child classes
        to define specific safety checks.
        Args:
            line (List[int]): A list of integers representing the line to be checked.
        Returns:
            bool: True if the line is considered safe, False otherwise.
        """
        raise NotImplementedError("Please implement in child classes.")
