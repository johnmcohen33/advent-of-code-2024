"""
Day 01 Part 01, Advent of Code 2024 in Python

Link to Site: https://adventofcode.com/2024/day/1

Upon pouring into the office, everyone confirms that the Chief Historian is indeed nowhere to be found. Instead, the Elves discover an assortment of notes and lists of historically significant locations! This seems to be the planning the Chief Historian was doing before he left. Perhaps these notes can be used to determine which locations to search?

Throughout the Chief's office, the historically significant locations are listed not by name but by a unique number called the location ID. To make sure they don't miss anything, The Historians split into two groups, each searching the office and trying to create their own complete list of location IDs.

There's just one problem: by holding the two lists up side by side (your puzzle input), it quickly becomes clear that the lists aren't very similar. Maybe you can help The Historians reconcile their lists?

For example:

3   4
4   3
2   5
1   3
3   9
3   3
Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are. Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

In the example list above, the pairs and distances would be as follows:

The smallest number in the left list is 1, and the smallest number in the right list is 3. The distance between them is 2.
The second-smallest number in the left list is 2, and the second-smallest number in the right list is another 3. The distance between them is 1.
The third-smallest number in both lists is 3, so the distance between them is 0.
The next numbers to pair up are 3 and 4, a distance of 1.
The fifth-smallest numbers in each list are 3 and 5, a distance of 2.
Finally, the largest number in the left list is 4, while the largest number in the right list is 9; these are a distance 5 apart.
To find the total distance between the left list and the right list, add up the distances between all of the pairs you found. In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!

Your actual left and right lists contain many location IDs. What is the total distance between your lists?
"""

def advent_of_code_day_1_part_1_v1(file_path: str) -> int:
    """
    given a filepath, find the total distance between the left and right lists in this file path.
    this function will load each list into memory, sort each respective list, and compute the summated distance
    between them.

    returns: summated distance between the two lists.
    """
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            line_by_line_data = data.split('\n')
            left, right = ([int(line.split()[0]) for line in line_by_line_data],
                           [int(line.split()[1]) for line in line_by_line_data])
            
            # sort the lists
            left.sort(), right.sort()

            # i/o to get data into two lists
            # Check preconditions: for instance, the lists should be of the same length.
            if len(left) != len(right):
                raise ValueError("Both lists must have the same number of elements.")

            # return the summation of distances between two lists
            return sum(abs(x - y) for x, y in zip(left, right))

    except FileNotFoundError as fe:
        raise FileNotFoundError("File not found.") from fe
    except ValueError as ve:
        raise ValueError("Lists could not be parsed in their current format.") from ve
    except TypeError as te:
        # If a non-numeric value is encountered, a TypeError may be raised.
        raise TypeError("Both lists must contain numbers.") from te
    except Exception as ex:
        raise Exception("") from ex


def advent_of_code_day_1_part_1_v2(file_path: str) -> int:
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

            left.sort()
            right.sort()

            # Calculate and return the sum of absolute differences between corresponding elements.
            return sum(abs(l - r) for l, r in zip(left, right))

    except FileNotFoundError as fe:
        raise FileNotFoundError(f"File not found: {file_path}") from fe

# Excute functions:

real_file_path = "./data/day01-pt01-input-real.txt.txt"
dummy_file_path = "./data/day01-pt01-input-dummy.txt.txt"

res_v1 = advent_of_code_day_1_part_1_v1(real_file_path)
res_v2 = advent_of_code_day_1_part_1_v2(real_file_path)

print("res_v1:", res_v1)
print("res_v2:", res_v2)