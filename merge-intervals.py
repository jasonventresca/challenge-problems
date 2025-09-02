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
        ret = []
        for (st, nd) in intervals:
            logger.debug(f'\t{st},\t{nd}')
            st_abs = False # Was start absorbed?
            nd_abs = False # Was end absorbed?
            for idx, (ps, pe) in enumerate(ret):
                '''
                [       ps      pe      ]
            ---------------------------------
                [       | st     |  nd  ]       # start is absorbed
                [ st    |   nd   |      ]       # end is absorbed
                '''
                # Should `start` be absorbed by a previous interval?
                if (st >= ps and st <= pe):
                    st = None
                    st_abs = True
                # Should `end` be absorbed by a previous interval?
                if (nd >= ps and nd <= pe):
                    nd = None
                    nd_abs = True

                if st is not None and nd is not None:
                    continue
                elif st is None and nd is None:
                    break
                elif st is None:
                    st = ps
                    ret[idx] = [ps, nd] # extend the previous interval to `end`
                elif nd is None:
                    nd = pe
                    ret[idx] = [st, pe] # extend the previous interval from `start`

            if st is not None and nd is not None:
                logger.debug(f'st_abs: {st_abs}')
                logger.debug(f'nd_abs: {nd_abs}')
                if st_abs or nd_abs:
                    logger.debug(f'not appending [{st}, {nd}]; was fully absorbed')
                else:
                    ret.append([st, nd])

        return ret

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
    logger.debug(f'result = {result}')
    assert expected_output == result
