#!/usr/bin/env python3
# https://leetcode.com/problems/basic-calculator
#   difficulty: Hard
#   topics: Math, String, Stack, Recursion
''' Run with the following commands (replace file name):
    $ pipenv shell
    $ py.test --log-cli-level=debug -v --tb=no basic-calculator.py
'''

from typing import List, Optional
import logging
from collections import defaultdict
import math

import pytest
from icecream import ic

logger = logging.getLogger(__name__)

class Solution:
    def calculate(self, s: str) -> int:
        logger.debug(f's: {s}')
        return 2

@pytest.mark.parametrize(
    'input_data, expected_output',
    [
        # Test case #1
        (
            # Input
            '1 + 1',
            # Expected Output
            2,
        ),
        # Test case #2
        (
            # Input
            ' 2-1 + 2 ',
            # Expected Output
            3,
        ),
        # Test case #3
        (
            # Input
            '(1+(4+5+2)-3)+(6+8)',
            # Expected Output
            23,
        ),
    ],
)
def test_case(input_data, expected_output):
    s = Solution()
    result = s.calculate(input_data)
    assert expected_output == result
