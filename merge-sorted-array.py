#!/usr/bin/env python3
# https://leetcode.com/problems/merge-sorted-array/

from typing import List

DEBUG = True

class Solution:
    @staticmethod
    def shift_right(arr, from_idx):
        """ shift each element right by one position, starting at from_idx """
        #size = len(arr)
        #for i in range(size - from_idx):
        #    idx =
        arr[from_idx+1:] = arr[from_idx:-1]
        arr[from_idx] = 0

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        print(nums1)
        self.shift_right(nums1, 0)
        print(nums1)

def main():
    test_cases = [
        # Test case #1
        (
            # Input
            (
                [1,2,3,0,0,0],
                3,
                [2,5,6],
                3
            ),
            # Expected Output
            [1,2,2,3,5,6],
        ),
    ]
    s = Solution()
    for (input_, expected_output) in test_cases:
        result = s.merge(*input_)
        assert (expected_output == result), \
            f'\nexpected: {expected_output}' \
            f'\n  result: {result}'
    print('All tests passed : )')

if __name__ == '__main__':
    main()
