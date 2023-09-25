# import all necessary libraries
from collections import defaultdict, deque
import math
import sys

from sw_easy import max_sum_subarray
from sw_med import longest_substring_with_k_distinct
from sw_hard import find_anagrams

# Define the test cases
MAX_SUM_SUBARRAY = [
    ([2, 1, 5, 1, 3, 2], 3),  # Expected output: 9 (because subarray [5, 1, 3] has the maximum sum)
    ([2, 3, 4, 1, 5], 2),     # Expected output: 7 (because subarray [3, 4] has the maximum sum)
    # Add more test cases as needed
]

LONGEST_SUBSTRING = [
    ("araaci", 2),  # Expected output: 4 (because substring "araa" has a maximum length with 2 distinct characters)
    ("araaci", 1),  # Expected output: 2 (either "aa" from "araa" or the last "ii" are the longest substrings with 1 distinct character)
    ("cbbebi", 3),  # Expected output: 5 (substring "cbbeb" or "bbebi" have the maximum length with 3 distinct characters)
    ("abcabc", 3),  # Expected output: 6 (the whole string has only 3 distinct characters)
    ("", 1),        # Expected output: 0 (empty string)
    # Add more test cases as needed
]

FIND_ANAGRAMS = [
    ("cbaebabacd", "abc"),  # Expected output: [0, 5]
    ("abab", "ab"),         # Expected output: [0, 1, 2]
    ("eidbaooo", "ab"),     # Expected output: [0, 1]
    ("eidboaoo", "ab"),     # Expected output: [0]
    # Add more test cases as needed
]

# some useful constants and functions
INF = int(1e9)
MOD = 1000000007

def read_int():
    return int(input().strip())

def read_ints():
    return list(map(int, input().strip().split()))

def solve(test_input):
    # process test_input
    pass

def main():

    # Run test cases for max_sum_subarray
    # for arr, K in MAX_SUM_SUBARRAY:
    #     result = max_sum_subarray(arr, K)
    #     print(f"For array {arr} with window size {K}, maximum sum is: {result}")

    # Run test cases for longest_substring_with_k_distinct
    # for s, K in LONGEST_SUBSTRING:
    #     result = longest_substring_with_k_distinct(s, K)
    #     print(f"For string '{s}' with {K} distinct characters, longest substring length is: {result}")

    # Run test cases for find_anagrams
    for s, pattern in FIND_ANAGRAMS:
        result = find_anagrams(s, pattern)
        print(f"For string '{s}' with pattern '{pattern}', anagram indices are: {result}")



if __name__ == "__main__":
    main()