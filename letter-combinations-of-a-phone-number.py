#!/usr/bin/env python3
# https://leetcode.com/problems/letter-combinations-of-a-phone-number
#   difficulty: Medium
#   topics: Hash Table, String, Backtracking
''' Run with the following commands (replace file name):
    $ pipenv shell
    $ py.test --log-cli-level=debug -v --tb=no letter-combinations-of-a-phone-number.py
'''

from typing import List, Optional
import logging
from collections import defaultdict
import math

import pytest
from icecream import ic

logger = logging.getLogger(__name__)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        def inner(rem: str, combos: List[str]) -> List[str]:
            ''' Take the input combos and cross them with each of the letters in the first digit of rem.
                Then, call recursivelly on the rest of rem. '''
            if len(rem) == 0:
                return combos
            dig = rem[0]
            ret = []
            for c in combos:
                for let in keypad[dig]:
                    ret.append(c + let)
            if len(rem) > 1:
                return inner(rem[1:], ret)
            else:
                return ret

        return inner(digits, ['',])
        logger.debug(f'input: {input_}')
        return False

@pytest.mark.parametrize(
    'input_data, expected_output',
    [
        # Test case #1
        (
            # Input
            "23",
            # Expected Output
            ["ad","ae","af","bd","be","bf","cd","ce","cf"],
        ),
        # Test case #2
        (
            # Input
            "2",
            # Expected Output
            ["a","b","c"],
        ),
    ],
)
def test_case(input_data, expected_output):
    s = Solution()
    result = s.letterCombinations(input_data)
    assert expected_output == result
