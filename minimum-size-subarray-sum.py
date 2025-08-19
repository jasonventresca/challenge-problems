#!/usr/bin/env python3
# https://leetcode.com/problems/minimum-size-subarray-sum/
#   difficulty: Medium
#   topics: Array, Binary Search, Sliding Window, Prefix Sum

from typing import List

DEBUG = True

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if DEBUG: print(f'target: {target}, nums: {nums}')
        return 0

def main():
    test_cases = [
        # Test case #1
        (
            # Input
            (7, [2,3,1,2,4,3]),
            # Expected Output
            2,
        ),
    ]
    s = Solution()
    for (input_, expected_output) in test_cases:
        result = s.minSubArrayLen(*input_)
        assert (expected_output == result), \
            f'\nexpected: {expected_output}' \
            f'\n  result: {result}'
    print('All tests passed : )')

if __name__ == '__main__':
    main()
