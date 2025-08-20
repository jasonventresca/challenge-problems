#!/usr/bin/env python3
# https://leetcode.com/problems/minimum-size-subarray-sum/
#   difficulty: Medium
#   topics: Array, Binary Search, Sliding Window, Prefix Sum

from typing import List

DEBUG = False

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ''' ___PSEUDOCODE___
        Step through the array, forming a sliding window of variable length.
        For each element in the main array, append it to the tail of the sliding window.
        After each append, check the sum of the sliding window.
        If the sliding window meets or exceeds the desired size:
            Compute the sliding window's cardinality, and low-water mark it.
            Then, remove the head element.
            Remove additional head elements, until the sum drops below the desired size.
        Proceed stepping through the main array.
        Return fewest or zero (if not set). '''

        if DEBUG: print(f'target: {target}, nums: {nums}')

        fewest = None
        window = list()
        for x in nums:
            if DEBUG: print(f'  x: {x}')
            window.append(x)
            if DEBUG: print(f'  window: {window}')
            if sum(window) >= target:
                # Prune head of window until below target.
                while sum(window) >= target:
                    # Record low water mark
                    card = len(window)
                    if fewest is None or card < fewest:
                        fewest = card

                    window = window[1:]

        return fewest or 0

def main():
    test_cases = [
        # Test case #1
        (
            # Input
            (7, [2,3,1,2,4,3]),
            # Expected Output
            2,
        ),
        # Test case #2
        (
            # Input
            (4, [1,4,4]),
            # Expected Output
            1,
        ),
        # Test case #3
        (
            # Input
            (11, [1,1,1,1,1,1,1,1]),
            # Expected Output
            0,
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
