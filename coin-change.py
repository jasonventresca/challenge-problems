#!/usr/bin/env python3
# https://leetcode.com/problems/coin-change
#   difficulty: Medium
#   topics: Array, Dynamic Programming, Breadth-First Search
''' Run with the following commands (replace file name):
    $ pipenv shell
    $ py.test --log-cli-level=debug -v --tb=no coin-change.py
'''

from typing import List, Optional
import logging
from collections import defaultdict
import math

import pytest
from icecream import ic

logger = logging.getLogger(__name__)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        DP Problem Definition
            dp[i] = fewest number of coins required to make i amount
        Base Cases
            dp[0] = 0
        DP Recurrence Relation
            dp[i] = min(dp[i-c] for c in coins) + 1
            *NB: If there's no c for which dp[i-c] is valid, return -1.
        Solution
            dp[amount]
        '''
        logger.debug(f'input: {coins}, {amount}')
        dp = [0] * (amount + 1)
        for i in range(1, amount+1):
            ways = []
            for c in coins:
                if c > i:
                    continue
                prev = dp[i-c]
                if prev == -1:
                    continue
                ways.append(prev + 1)
            if ways:
                dp[i] = min(ways)
            else:
                dp[i] = -1
        return dp[amount]

@pytest.mark.parametrize(
    'input_data, expected_output',
    [
        # Test case #1
        (
            # Input
            (
                # coins
                [1,2,5],
                # amount
                11,
            ),
            # Expected Output
            3,
        ),
        # Test case #2
        (
            # Input
            (
                # coins
                [2],
                # amount
                3,
            ),
            # Expected Output
            -1,
        ),
        # Test case #2
        (
            # Input
            (
                # coins
                [1],
                # amount
                0,
            ),
            # Expected Output
            0,
        ),
    ],
)
def test_case(input_data, expected_output):
    s = Solution()
    result = s.coinChange(*input_data)
    assert expected_output == result
