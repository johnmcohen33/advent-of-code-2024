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

from typing import Callable, List, Tuple
from helpers import create_lists_from_file_v1, create_lists_from_file_v2

# Define a type alias for injectable for clarity.
ListCreator = Callable[[str], Tuple[List[int], List[int]]]

class TotalDistanceCalculator:
    
    def __init__(self, list_creator: ListCreator = create_lists_from_file_v2):
        """
        :param list_creator: A function that takes a file path and returns a tuple of two lists of integers.
                             Defaults to the v1 implementation.
        """
        self.list_creator = list_creator

    def get_total_distance(self, file_path: str) -> int:
        """
        given a filepath, find the total distance between the left and right lists in this file path.
        this function will load each list into memory, sort each respective list, and compute the summated distance
        between them.

        returns: summated distance between the two lists.
        """

        left, right = self.list_creator(file_path)
        
        # sort the lists
        left.sort(), right.sort()

        # return the summation of distances between two lists
        return sum(abs(x - y) for x, y in zip(left, right))

# Excute functions:

real_file_path = f"/Users/johncohen/Documents/Documents/Job_Hunt_2025/SE_Job_Hunt/advent-of-code-2024/data/day01-pt01-input-real.txt"
dummy_file_path = f"/Users/johncohen/Documents/Documents/Job_Hunt_2025/SE_Job_Hunt/advent-of-code-2024/data/day01-pt01-input-dummy.txt"
tDistanceCalc_v1 = TotalDistanceCalculator(create_lists_from_file_v1)
tDistanceCalc_v2 = TotalDistanceCalculator(create_lists_from_file_v2)

res_v1 = tDistanceCalc_v1.get_total_distance(real_file_path)
res_v2 = tDistanceCalc_v2.get_total_distance(real_file_path)

print("res_v1:", res_v1)
print("res_v2:", res_v2)