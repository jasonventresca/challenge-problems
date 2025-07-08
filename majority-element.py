#!/usr/bin/env python3
# https://leetcode.com/problems/majority-element/
#   difficulty: Easy
#   topics: Array, Hash Table, Divide and Conquer, Sorting, Counting

from typing import List

import pytest

DEBUG = True

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if DEBUG: print(f'### nums = {nums} ###')
        return False

@pytest.mark.parametrize(
    'input_data, expected_output',
    [
        (
            [3,2,3],
            3,
        ),
        (
            [2,2,1,1,1,2,2],
            2,
        ),
    ],
)
def test_case(input_data, expected_output):
    s = Solution()
    result = s.majorityElement(input_data)
    assert expected_output == result
