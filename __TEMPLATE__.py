#!/usr/bin/env python3
# https://leetcode.com/??? <-- TODO: Problem URL goes here.
#   difficulty: TODO: difficulty level goes here
#   topics: TODO: topics go here
''' Run with the following commands (replace file name):
    $ pipenv shell
    $ py.test --log-cli-level=debug -v --tb=no __TEMPLATE__.py
'''

from typing import List
import logging
from collections import defaultdict
import math

import pytest
from icecream import ic

logger = logging.getLogger(__name__)

class Solution:
    def problem(self, input_): # TODO: Paste leetcode-provided method here.
        logger.debug(f'problem(): input_ = {input_}')
        return False

@pytest.mark.parametrize(
    'input_data, expected_output',
    [
        # Test case #1
        (
            # Input
            'foo',
            # Expected Output
            'bar',
        ),
        # Test case #2
        (
            # Input
            'hello',
            # Expected Output
            'world',
        ),
    ],
)
def test_case(input_data, expected_output):
    s = Solution()
    result = s.problem(input_data)
    assert expected_output == result
