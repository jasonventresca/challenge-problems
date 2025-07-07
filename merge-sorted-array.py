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
        if DEBUG: print(f'nums1: {nums1}')
        if DEBUG: print(f'nums2: {nums2}')
        ######### Definitions #########
        a = nums1
        a_i = 0 # current index of a
        a_val = None # value at current index of a
        b = nums2
        b_i = 0 # current index of b
        b_val = None # value at current index of b
        ###############################
        '''
        Case 1:
            All of b is sandwiched into a somewhere before the end of the original, non-zero elements of a.
        Case 2:
            Some of b is appended past the end of the non-zero elements of a.
        '''
        if DEBUG: print(f'before:\n\t{a}')
        # Step through each element in b
        # Starting at head of a, advance until the current element of b is greater than or equal to the the current element of a
        # Then, shift the rest of a right, and insert the b value into the open location
        while b_i < n:
            while a_i < m + b_i and b_i < n:
                a_val = a[a_i]
                b_val = b[b_i]
                if DEBUG: print(f'a[{a_i}]: {a_val}')
                if DEBUG: print(f'b[{b_i}]: {b_val}')
                if b_val <= a_val:
                    self.shift_right(a, a_i)
                    a[a_i] = b_val
                    b_i += 1
                else:
                    pass

                #if DEBUG: print(f'a: {a}')
                if DEBUG: print(f'nums1: {nums1}')
                if DEBUG: print()
                a_i += 1

            if DEBUG: print('--- surpassed original a ---')
            if b_i >= n:
                break

            a_val = a[a_i]
            b_val = b[b_i]
            if DEBUG: print(f'a[{a_i}]: {a_val}')
            if DEBUG: print(f'b[{b_i}]: {b_val}')
            a[a_i] = b_val
            a_i += 1
            b_i += 1

        if DEBUG: print(f'after:\n\t{nums1}')
        return nums1

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
        # Test case #2
        (
            # Input
            (
                [2,0],
                1,
                [1],
                1
            ),
            # Expected Output
            [1,2],
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
