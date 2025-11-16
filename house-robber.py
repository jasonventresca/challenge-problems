#!/usr/bin/env python3
# https://leetcode.com/problems/house-robber
#   difficulty: Medium
#   topics: Array, Dynamic Programming
''' Run with the following commands (replace file name):
    $ pipenv shell
    $ py.test --log-cli-level=debug -v --tb=no house-robber.py
'''

from typing import List, Optional
import logging
from collections import defaultdict
import math

import pytest
from icecream import ic

logger = logging.getLogger(__name__)

'''
e.g. [2, 7, 9, 3, 1]

0. base case: no homes remaining? record amount in money bag
1. for each house, decide whether to rob it or not
2. decision is, either:
3.      rob it : money += nums[i] + rob(nums[i+2])
4.      skip it: money += rob(nums[i+1])

Translating this^ to a 1D-DP (working from bottom-up):
5. dp[i] = max(
                nums[i] + dp[i-2],
                dp[i-1]
            )
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.rob_recursive(nums)
    def rob_recursive(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def helper(i: int) -> int:
            if i == n-1:
                return nums[i]
            if i == n-2:
                return max(nums[i], nums[i+1])
            if i in memo:
                return memo[i]
            ret = max(
                nums[i] + helper(i+2),
                helper(i+1)
            )
            memo[i] = ret
            return ret
        return helper(0)
    def rob_iterative(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n # dp[i] represents how much we can steal from houses 0..i
        dp[0] = nums[0] # one house -> only one option
        dp[1] = max(dp[0], nums[1]) # two houses -> only first or second
        for i in range(2, n):
            dp[i] = max(
                nums[i] + dp[i-2],
                dp[i-1]
            )
        return dp[-1]

@pytest.mark.parametrize(
    'input_data, expected_output',
    [
        # Test case #1
        (
            # Input
            [1,2,3,1],
            # Expected Output
            4,
        ),
        # Test case #2
        (
            # Input
            [2,7,9,3,1],
            # Expected Output
            12,
        ),
    ],
)
def test_case(input_data, expected_output):
    s = Solution()
    result = s.rob(input_data)
    assert expected_output == result
