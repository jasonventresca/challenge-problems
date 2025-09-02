#!/usr/bin/env python3
# https://leetcode.com/problems/merge-intervals
#   difficulty: Medium
#   topics: Array, Sorting
''' Run with the following commands (replace file name):
    $ pipenv shell
    $ py.test --log-cli-level=debug -v --tb=no merge-intervals.py
'''

from typing import List
import logging
from collections import defaultdict
import math

import pytest
from icecream import ic

logger = logging.getLogger(__name__)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        logger.debug(f'input: {intervals}')
        return []

@pytest.mark.parametrize(
    'input_data, expected_output',
    [
        # Test case #1
        (
            # Input
            [[1,3],[2,6],[8,10],[15,18]],
            # Expected Output
            [[1,6],[8,10],[15,18]],
        ),
        # Test case #2
        (
            # Input
            [[1,4],[4,5]],
            # Expected Output
            [[1,5]],
        ),
        # Test case #3
        (
            # Input
            [[4,7],[1,4]],
            # Expected Output
            [[1,7]],
        ),
    ],
)
def test_case(input_data, expected_output):
    s = Solution()
    result = s.merge(input_data)
    assert expected_output == result
