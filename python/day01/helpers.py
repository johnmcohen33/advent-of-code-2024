from typing import Optional, Tuple, List

def create_lists_from_file_v1(file_path: str) -> Tuple[Optional[List[int]], Optional[List[int]]]:
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            line_by_line_data = data.split('\n')
            left, right = ([int(line.split()[0]) for line in line_by_line_data],
                        [int(line.split()[1]) for line in line_by_line_data])
            return left, right
    except FileNotFoundError as fe:
            raise FileNotFoundError("File not found.") from fe
    except ValueError as ve:
        raise ValueError("Lists could not be parsed in their current format.") from ve
    except TypeError as te:
        # If a non-numeric value is encountered, a TypeError may be raised.
        raise TypeError("Both lists must contain numbers.") from te
    except IndexError as ie:
        # TODO: Is this a bad error? Should we just fix this for the user?
        raise IndexError("Ensure the list does not have whitespace trailing the file.") from ie
    
def create_lists_from_file_v2(file_path: str) -> Tuple[Optional[List[int]], Optional[List[int]]]:
    """
    Reads a file where each non-empty line contains exactly two integers separated by whitespace.
    It collects the left and right numbers into separate lists, sorts both lists, and returns the
    sum of the absolute differences between corresponding elements.
    
    Args:
        file_path: The path to the input file.
    
    Returns:
        The sum of the absolute differences between corresponding integers in the sorted lists.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If a line does not contain exactly two integer values or conversion fails.
    """
    try:
        with open(file_path, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]
        
            left, right = [], []
            
            # Process each line
            for line in lines:
                parts = line.split()
                if len(parts) != 2:
                    raise ValueError(f"Line does not contain exactly two values: '{line}'")
                
                try:
                    left_val = int(parts[0])
                    right_val = int(parts[1])
                except ValueError as ve:
                    raise ValueError(f"Could not convert values to int in line: '{line}'") from ve
                
                left.append(left_val)
                right.append(right_val)

                # Although both lists are built from the same source, it's safe to check their lengths.
                if len(left) != len(right):
                    raise ValueError("Parsed lists have different lengths.")

            return left, right

    except FileNotFoundError as fe:
        raise FileNotFoundError(f"File not found: {file_path}") from fe