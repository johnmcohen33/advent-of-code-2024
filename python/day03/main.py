import re
from typing import Iterator, Tuple
from dataclasses import dataclass
from functools import reduce

class Instruction:
    """Base instruction class."""
    pass

@dataclass
class Multiply(Instruction):
    """Represents a Multiply instruction."""
    A: int
    B: int

@dataclass
class Pause(Instruction):
    """Represents a Pause instruction."""
    pass

@dataclass
class Resume(Instruction):
    """Represents a Resume instruction."""
    pass

class FileLoader:
    """Handles file reading operations."""
    
    @staticmethod
    def load_text(file_path: str) -> str:
        """Reads a file and returns its content as a string."""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: Could not open file: {file_path}")
        except IOError as e:
            print(f"Error reading file {file_path}: {e}")
        return ""


class ValueExtractor:
    """Handles extracting values from text using regex."""

    CONTROL_PATTERN = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)|(?:\w*)?(do|don't)\(\s*\)"

    @staticmethod
    def extract_instructions(text: str) -> Iterator[Instruction]:
        """
        Extracts:
        - `"a, b"` from `mul(a, b)`
        - `"do"` from `do()`
        - `"don't"` from `don't()`
        """
        try:
            matches = re.findall(ValueExtractor.CONTROL_PATTERN, text)
            extracted_values = []

            for num1, num2, keyword in matches:
                if num1 and num2:
                    extracted_values.append(Multiply(int(num1), int(num2)))
                elif keyword:
                    if keyword == "do":
                        extracted_values.append(Resume())
                    if keyword == "don't":
                        extracted_values.append(Pause())

            return extracted_values
        except (ValueError, re.error) as e:
            print(f"Error processing regex text: {e}")
            return []


class MultiplicationProcessor:
    """Processes extracted values and calculates sums based on conditions."""

    @staticmethod
    def process_instruction(acc: Tuple[int, bool], instruction: Instruction) -> Tuple[int, bool]:
        _sum, include = acc
        """ Takes an instruction and returns the current sum and whether future multiplications should be included. """
        if isinstance(instruction, Pause):
            return _sum, False
        elif isinstance(instruction, Resume):
            return _sum, True
        elif isinstance(instruction, Multiply) and include:
            return _sum + (instruction.A * instruction.B), include
        return acc

    @staticmethod
    def sum_products(instructions: Iterator[Instruction]) -> int:
        reduced = reduce(MultiplicationProcessor.process_instruction, instructions, (0, True))
        return reduced[0] # first element is the sum
       
def main():
    """
    Main function to orchestrate file reading, extracting values, and computing results.
    """
    dummy_file_path = "/Users/johncohen/Documents/Documents/Job_Hunt_2025/SE_Job_Hunt/advent-of-code-2024/data/day03-pt01-input-dummy.txt"
    real_file_path = "/Users/johncohen/Documents/Documents/Job_Hunt_2025/SE_Job_Hunt/advent-of-code-2024/data/day03-pt01-input-real.txt"

    # Load file contents
    text = FileLoader.load_text(real_file_path)

    # Extract values
    instructions = ValueExtractor.extract_instructions(text)

    print("Part1 Result: ", MultiplicationProcessor.sum_products((i for i in instructions if isinstance(i, Multiply))))
    print("Part2 Result: ", MultiplicationProcessor.sum_products(instructions))
    
if __name__ == "__main__":
    main()