#!/usr/bin/env python3
# https://leetcode.com/problems/set-matrix-zeroes
#   difficulty: Medium
#   topics: Array, Hash Table, Matrix
''' Run with the following commands (replace file name):
    $ pipenv shell
    $ py.test --log-cli-level=debug -v --tb=no set-matrix-zeroes.py
'''

from typing import List, Optional
import logging
from collections import defaultdict
import math

import pytest
from icecream import ic

logger = logging.getLogger(__name__)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ''' ___PSEUDOCODE___
            1st pass through the matrix:
                - Find all zeroes, note their row and column indexes
                - Store the row and column indexes containing zeroes in two unique sets: zr, zc
            2nd pass:
                - For each element (r,c), set to zero `if r in zr or c in zc`
            Return the in-place updated matrix '''
        logger.info(f'input: {matrix}')
        zr, zc = set(), set()
        for phase in (1, 2):
            for i, row in enumerate(matrix):
                for j, cell in enumerate(row):
                    if phase == 1:
                        logger.debug(f'{i}\t{j}:\t{cell}')
                        if cell == 0:
                            zr.add(i)
                            zc.add(j)
                    elif phase == 2:
                        if i in zr or j in zc:
                            matrix[i][j] = 0

        return matrix

@pytest.mark.parametrize(
    'input_data, expected_output',
    [
        # Test case #1
        (
            # Input
            [[1,1,1],[1,0,1],[1,1,1]],
            # Expected Output
            [[1,0,1],[0,0,0],[1,0,1]],
        ),
        # Test case #2
        (
            # Input
            [[0,1,2,0],[3,4,5,2],[1,3,1,5]],
            # Expected Output
            [[0,0,0,0],[0,4,5,0],[0,3,1,0]],
        ),
    ],
)
def test_case(input_data, expected_output):
    s = Solution()
    result = s.setZeroes(input_data)
    assert expected_output == result
