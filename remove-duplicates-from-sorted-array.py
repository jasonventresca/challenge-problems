#!/usr/bin/env python3
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#   difficulty: Easy
#   topics: Array, Two Pointers

DEBUG = True

from typing import List

class Solution:
    def easy(self, nums: List[int]) -> int:
        dedup = list(sorted(set(nums)))
        for i, v in enumerate(dedup):
            nums[i] = dedup[i]
        k = len(dedup)
        return k

    def hard(self, nums: List[int]) -> int:
        i = 0
        k = len(nums)
        prev = None
        dup = False
        while i < k:
            if DEBUG: print(f'''
            i = {i}
            k = {k}
            nums = {nums}
            cur = {nums[i]}
            prev = {prev}
            ---
            '''.strip())
            if i > 0:
                prev = nums[i-1]

            if prev is not None and nums[i] == prev:
                nums.pop(i)
                dup = True
                k -= 1
            else:
                dup = False

            if not dup:
                i += 1

        return k

    def removeDuplicates(self, nums: List[int]) -> int:
        if DEBUG: print(f'### input: {nums}')

        return self.hard(nums)

def main():
    test_cases = [
        # Test case #1
        (
            # Input
            [1,1,2],
            # Expected Output
            [1,2],
        ),
        # Test case #2
        (
            # Input
            [0,0,1,1,1,2,2,3,3,4],
            # Expected Output
            [0,1,2,3,4],
        ),
    ]
    s = Solution()
    for (input_, expected_output) in test_cases:
        k = s.removeDuplicates(input_)

        error_msg = f'\nexpected: {expected_output}\n  result: {input_}'
        assert k == len(expected_output), error_msg
        assert (expected_output == input_[:k]), error_msg
    print('All tests passed : )')

if __name__ == '__main__':
    main()
