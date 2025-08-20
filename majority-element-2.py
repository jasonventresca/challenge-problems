#!/usr/bin/env python3
# https://leetcode.com/problems/majority-element-ii/
#   difficulty: Medium
#   topics: Array, Hash Table, Sorting, Counting

from typing import List
import logging
from collections import defaultdict
import math

import pytest
from icecream import ic

logger = logging.getLogger(__name__)

class Solution:
    def easy(self, nums: List[int]) -> int:
        logger.debug(f'### nums = {nums} ###')
        counts = defaultdict(int)
        total = 0
        for n in nums:
            counts[n] += 1
            total += 1

        counts = dict(counts)
        third = 1 + math.floor(total / 3)
        logger.debug(ic.format(counts, total, third))
        ret = []
        for k, v in counts.items():
            if v >= third:
                ret.append(k)

        return ret

    def hard(self, nums: List[int]) -> int:
        # Implement the "triplet-off" algorithm,
        cand1 = cand2 = None
        cnt1 = cnt2 = 0

        # Pass 1: find up to two candidates
        for x in nums:
            if x == cand1:
                cnt1 += 1
            elif x == cand2:
                cnt2 += 1
            elif cnt1 == 0:
                cand1, cnt1 = x, 1
            elif cnt2 == 0:
                cand2, cnt2 = x, 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        # Pass 2: verify
        cnt1 = cnt2 = 0
        for x in nums:
            if x == cand1:
                cnt1 += 1
            elif x == cand2:
                cnt2 += 1

        res = []
        n_third = len(nums) // 3
        if cnt1 > n_third:
            res.append(cand1)
        if cnt2 > n_third:
            res.append(cand2)

        return res

    def majorityElement(self, nums: List[int]) -> int:
        return self.hard(nums)

@pytest.mark.parametrize(
    'input_data, expected_output',
    [
        (
            [3,2,3],
            [3],
        ),
        (
            [1],
            [1],
        ),
        (
            [1,2],
            [1,2],
        ),
    ],
)
def test_case(input_data, expected_output):
    s = Solution()
    result = s.majorityElement(input_data)
    assert expected_output == result
