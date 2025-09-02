#!/usr/bin/env python3
# https://leetcode.com/problems/gas-station
#   difficulty: Medium
#   topics: Array, Greedy
''' Run with the following commands (replace file name):
    $ pipenv shell
    $ py.test --log-cli-level=debug -v --tb=no gas-station.py
'''

from typing import List, Optional
import logging
from collections import defaultdict
import math

import pytest
from icecream import ic

logger = logging.getLogger(__name__)

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        logger.debug(f'gas: {gas}, cost: {cost}')
        return False

@pytest.mark.parametrize(
    'input_data, expected_output',
    [
        # Test case #1
        (
            # Input
            (
                # gas
                [1,2,3,4,5],
                # cost
                [3,4,5,1,2],
            ),
            # Expected Output
            3,
        ),
        # Test case #1
        (
            # Input
            (
                # gas
                [2,3,4],
                # cost
                [3,4,3],
            ),
            # Expected Output
            -1,
        ),
    ],
)
def test_case(input_data, expected_output):
    s = Solution()
    result = s.canCompleteCircuit(*input_data)
    assert expected_output == result
