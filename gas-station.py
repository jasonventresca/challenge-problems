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
        ''' ___PSEUDOCODE___
            1. Step through each element i of gas and cost, respectively.
            2. Call a recursive function that returns the remaining gas in the tank
               after visiting the next station; or else bails early if the next station
               cannot be reached (i.e. balance < 0).
            3. Return i if the recursive function returns a non-negative number.
            4. If the for loop is exhausted, return -1. '''
        for i, g in enumerate(gas):
            gas_loop = gas[i:] + gas[:i] if i != 0 else gas
            cost_loop = cost[i:] + cost[:i] if i != 0 else cost
            logger.debug(f'i: {i}')
            logger.debug(f'\tgas_loop: {gas_loop}')
            logger.debug(f'\tcost_loop: {cost_loop}')
            result = self.toNextStop(gas_loop, cost_loop, 0)
            logger.debug(f'result: {result}')
            if result >= 0:
                return i

        return -1

    @classmethod
    def toNextStop(cls, gas, cost, tank):
        tank = tank - cost[0] + gas[0]
        if tank >= 0:
            if len(gas) > 1:
                # Made it to the next station...
                return cls.toNextStop(
                    gas[1:],
                    cost[1:],
                    tank,
                )
            else:
                # Completed the loop :)
                return tank
        else:
            # Ran out of gas :(
            return tank

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
        # Test case #2
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
