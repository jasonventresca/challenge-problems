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
        logger.warning(f's: {s}')
        logger.warning('-' * 30)
        digits = tuple('1234567890')
        rhs = None
        operator = None
        result = 0
        prev = None
        stop = False
        for i, c in enumerate(s):
            if stop:
                break

            logger.info(f'c: {c}')
            if c in digits or c == '(':
                sign = -1 if prev == '-' else 1
                if c in digits:
                    expr = sign * int(c)
                else: # c == '('
                    logger.debug(f'-> stopping now, before next c: {s[i+1] if i < len(s) else "$"}')
                    logger.debug('x' * 30)
                    expr = sign * self.calculate(s[i+1:])
                    stop = True

                if operator is None:
                    result += expr
                elif operator in ('+', '-'):
                    rhs = expr
                    op_sign = 1 if operator == '+' else -1
                    result += op_sign * rhs
                    operator, rhs = None, None
                else:
                    raise ValueError(f'Unexpected operator: "{operator}" !')
            elif c == ')':
                return result
            elif c == '+':
                operator = '+'
            elif c == '-':
                #operator = '-'
                prev = '-'
            elif c == ' ':
                if prev == '-':
                    operator = '-'
                    prev = None
            else:
                raise ValueError(f'Parser got unexpected token: "{c}" !')

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
        # Jason's tinkering case A
        (
            # Input
            '1 + 1 + 2 + 4 + 8',
            # Expected Output
            16,
        ),
        # Test case #2
        (
            # Input
            ' 2-1 + 2 ',
            # Expected Output
            3,
        ),
        # Jason's tinkering case B
        (
            # Input
            '1 + 2 - 3 - 4',
            # Expected Output
            -4,
        ),
        # Jason's tinkering case C
        (
            # Input
            '1 + -3',
            # Expected Output
            -2,
        ),
        # Jason's tinkering case D
        (
            # Input
            '1 - -3',
            # Expected Output
            4,
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
