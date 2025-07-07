#!/usr/bin/env python3
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

DEBUG = True

from typing import List

class Solution:
    def easy(self, nums: List[int]) -> int:
        dedup = list(sorted(set(nums)))
        for i, v in enumerate(dedup):
            nums[i] = dedup[i]
        k = len(dedup)
        return k

    def removeDuplicates(self, nums: List[int]) -> int:
        if DEBUG: print(f'### input: {nums}')

        return self.easy(nums)

def main():
    test_cases = [
        # Test case #1
        (
            # Input
            [1,1,2],
            # Expected Output
            [1,2],
        ),
    ]
    s = Solution()
    for (input_, expected_output) in test_cases:
        k = s.removeDuplicates(input_)
        assert k == len(expected_output)
        assert (expected_output == input_[:k]), \
            f'\nexpected: {expected_output}' \
            f'\n  result: {input_}'
    print('All tests passed : )')

if __name__ == '__main__':
    main()
