from typing import Generator, List

def generate_nums_from_file(file_path: str) -> Generator[List[int], any, None]:
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

def is_safe_line(line: List[int]):
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

def get_safe_lines_from_file(file_path: str) -> int:
    return sum(1 for line in generate_nums_from_file(file_path) if is_safe_line(line))

dummy_file_path = f"/Users/johncohen/Documents/Documents/Job_Hunt_2025/SE_Job_Hunt/advent-of-code-2024/data/day02-pt01-input-dummy.txt"
real_file_path = f"/Users/johncohen/Documents/Documents/Job_Hunt_2025/SE_Job_Hunt/advent-of-code-2024/data/day02-pt01-input-real.txt"


numSafe = get_safe_lines_from_file(real_file_path)
print(numSafe)