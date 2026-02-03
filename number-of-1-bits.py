#!/usr/bin/env python3
# https://leetcode.com/problems/number-of-1-bits
#   difficulty: Easy
#   topics: Divide and Conquer, Bit Manipulation
''' Run with the following commands (replace file name):
    $ pipenv shell
    $ py.test --log-cli-level=debug -v --tb=no number-of-1-bits.py
'''

from typing import List, Optional
import logging
from collections import defaultdict
import math

import pytest
from icecream import ic

logger = logging.getLogger(__name__)

class Solution:
    def hammingWeight(self, n: int) -> int:
        logger.debug(f'input: {n}')
        if n == 0:
            return 0
        # e.g. 1 -> 1, 2 -> 2, 3 -> 2, ...
        bits = math.floor(math.log(n, 2)) + 1
        count = 0
        for b in range(bits):
            mask = 1 << b
            if n & mask:
                count += 1
        return count

@pytest.mark.parametrize(
    'input_data, expected_output',
    [
        # Test case #1
        (
            # Input
            11,
            # Expected Output
            3,
        ),
        # Test case #2
        (
            # Input
            128,
            # Expected Output
            1,
        ),
        # Test case #3
        (
            # Input
            2147483645,
            # Expected Output
            30,
        ),
    ],
)
def test_case(input_data, expected_output):
    s = Solution()
    result = s.hammingWeight(input_data)
    assert expected_output == result
