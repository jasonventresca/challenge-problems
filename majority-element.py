#!/usr/bin/env python3
# https://leetcode.com/problems/majority-element/
#   difficulty: Easy
#   topics: Array, Hash Table, Divide and Conquer, Sorting, Counting

from typing import List
import logging
from collections import defaultdict
import math

import pytest
from icecream import ic

logger = logging.getLogger(__name__)

class Solution:
    def easy(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        total = 0
        for n in nums:
            counts[n] += 1
            total += 1

        counts = dict(counts)
        half = 1 + math.floor(total / 2)
        logger.debug(ic.format(counts, total, half))
        for k, v in counts.items():
            if v >= half:
                return k

    def hard(self, nums: List[int]) -> int:
        # Implement the "pair-off" algorithm,
        # a.k.a. Boyer-Moore Majority Vote algorithm
        cand = None # candidate
        count = 0
        for n in nums:
            if count == 0:
                cand = n
                count = 1
            elif cand == n:
                count += 1
            else:
                count -= 1

        return cand

    def majorityElement(self, nums: List[int]) -> int:
        logger.debug(f'### nums = {nums} ###')
        return self.hard(nums)

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
        (
            [6,5,5],
            5,
        ),
        (
            [3,3,4],
            3,
        ),
    ],
)
def test_case(input_data, expected_output):
    s = Solution()
    result = s.majorityElement(input_data)
    assert expected_output == result
