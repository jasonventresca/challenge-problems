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
        logger.debug('-' * 30)
        digits = tuple('1234567890')
        rhs = None
        operator = None
        result = 0
        for c in s:
            logger.debug(f'c: {c}')
            if c in digits:
                logger.debug('-> it\'s a digit')
                if operator is None:
                    result += int(c)
                elif operator == '+':
                    rhs = int(c)
                    result += rhs
                    operator, rhs = None, None
                else:
                    raise ValueError('Unexpected operator: "{operator}" !')
            elif c == '(':
                raise NotImplementedError('(')
            elif c == ')':
                raise NotImplementedError(')')
            elif c == '+':
                operator = '+'
            elif c == '-':
                raise NotImplementedError('-')
            elif c == ' ':
                pass
            else:
                raise ValueError('Parser got unexpected token: "{c}" !')

        return result

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
        (
            # Input
            '1 + 1 + 2',
            # Expected Output
            4,
        ),
        ## Test case #2
        #(
        #    # Input
        #    ' 2-1 + 2 ',
        #    # Expected Output
        #    3,
        #),
        ## Test case #3
        #(
        #    # Input
        #    '(1+(4+5+2)-3)+(6+8)',
        #    # Expected Output
        #    23,
        #),
    ],
)
def test_case(input_data, expected_output):
    s = Solution()
    result = s.calculate(input_data)
    assert expected_output == result
