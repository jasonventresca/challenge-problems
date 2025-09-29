#!/usr/bin/env python3
# https://leetcode.com/problems/average-of-levels-in-binary-tree
#   difficulty: Easy
#   topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
''' Run with the following commands (replace file name):
    $ pipenv shell
    $ py.test --log-cli-level=debug -v --tb=no average-of-levels-in-binary-tree.py
'''

from typing import List, Optional
import logging
from collections import defaultdict
import math

import pytest
from icecream import ic

logger = logging.getLogger(__name__)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return ', '.join([
            str(self.val),
            self.left.__str__(),
            self.right.__str__(),
        ])

    def __str__(self):
        return self.__repr__()

class Solution:
    @classmethod
    def avgOfLowerLevels(cls, nodes: List[TreeNode]) -> List[float]:
        vals = []
        for x in nodes:
            if x and x.val:
                vals.append(str(x.val))
        msg = ','.join(vals)

        logger.debug(f'avgOfLowerLevels( {msg} )')
        sum_ = 0
        count = 0
        level_below = []
        for node in nodes:
            if node and node.val:
                sum_ += node.val
                count += 1
                level_below += [
                    node.left,
                    node.right,
                ]

        avg = float(sum_) / float(count) if count else float(0)
        ret = [avg]
        if level_below and any([x is not None for x in level_below]):
            ret += cls.avgOfLowerLevels(level_below)

        logger.debug(f' -> about to return ret ({type(ret)}): {ret}')
        return ret

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        logger.debug(f'root: {root}')
        if not root.val:
            return 0

        return self.avgOfLowerLevels([
            root,
        ])

@pytest.mark.parametrize(
    'input_data, expected_output',
    [
        # Test case #1
        (
            # Input
            TreeNode(
                val=3,
                left=TreeNode(val=9),
                right=TreeNode(
                    val=20,
                    left=TreeNode(val=15),
                    right=TreeNode(val=7)
                ),
            ),
            # Expected Output
            [3, 14.5, 11],
        ),
    ],
)
def test_case(input_data, expected_output):
    s = Solution()
    result = s.averageOfLevels(input_data)
    assert expected_output == result
