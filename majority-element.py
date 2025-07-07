#!/usr/bin/env python3
# https://leetcode.com/problems/majority-element/
#   difficulty: Easy
#   topics: Array, Hash Table, Divide and Conquer, Sorting, Counting

from typing import List

DEBUG = True

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if DEBUG: print(f'### nums = {nums} ###')
        return False

def main():
    test_cases = [
        # Test case #1
        (
            # Input
            [3,2,3],
            # Expected Output
            3,
        ),
        # Test case #1
        (
            # Input
            [2,2,1,1,1,2,2],
            # Expected Output
            2,
        ),
    ]
    s = Solution()
    for (input_, expected_output) in test_cases:
        result = s.majorityElement(input_)
        assert (expected_output == result), \
            f'\nexpected: {expected_output}' \
            f'\n  result: {result}'
    print('All tests passed : )')

if __name__ == '__main__':
    main()
