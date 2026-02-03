#!/usr/bin/env python3
# https://leetcode.com/problems/climbing-stairs
#   difficulty: Easy
#   topics: Math, Dynamic Programming, Memoization
''' Run with the following commands (replace file name):
    $ pipenv shell
    $ py.test --log-cli-level=debug -v --tb=no climbing-stairs.py
'''

from typing import List, Optional
import logging
from collections import defaultdict
import math

import pytest
from icecream import ic

logger = logging.getLogger(__name__)

class Solution:
    def climbStairs(self, n: int) -> int:
        return self.recursive(n)

    def recursive(self, n: int) -> int:
        '''
        Implement using recursion and memoization.
        Recursive function starts at n and recurses down to 2 and 1 (base cases).
        '''
        memo = {}
        def inner(k):
            if k in memo:
                return memo[k]
            elif k == 0:
                return 0
            elif k == 1:
                return 1
            elif k == 2:
                return 2

            ret = inner(k-1) + inner(k-2)
            memo[k] = ret

            return ret

        return inner(n)

    def dp1(self, n: int) -> int:
        '''
        DP problem definition
            dp[i]: # of distinct ways to reach step i+1
        Base case
            dp[0] = 1
            dp[1] = 2
        Recurrence relation
            dp[i] = dp[i-1] + dp[i-2]
        Solution
            for i in range(n+1)
        '''
        logger.debug(f'input: {n}')
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

    def dp0(self, n: int) -> int:
        logger.debug(f'input: {n}')
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n-1]

@pytest.mark.parametrize(
    'input_data, expected_output',
    [
        # Test case #1
        (
            # Input
            2,
            # Expected Output
            2,
        ),
        # Test case #2
        (
            # Input
            3,
            # Expected Output
            3,
        ),
        # Test case #3
        #   1 + 1 + 1 + 1
        #   1 + 1 + 2
        #   1 + 2 + 1
        #   2 + 1 + 1
        #   2 + 2
        (
            # Input
            4,
            # Expected Output
            5,
        ),
    ],
)
def test_case(input_data, expected_output):
    s = Solution()
    result = s.climbStairs(input_data)
    assert expected_output == result
