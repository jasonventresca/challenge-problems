#!/usr/bin/env python3
# https://leetcode.com/problems/binary-tree-right-side-view
#   difficulty: Medium
#   topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
''' Run with the following commands (replace file name):
    $ pipenv shell
    $ py.test --log-cli-level=debug -v --tb=no binary-tree-right-side-view.py
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        print(f'root: {root}')
        return self.rightmostOfLevelAndBelow([root])

    @classmethod
    def rightmostOfLevelAndBelow(cls, nodes: List[TreeNode]) -> List[int]:
        level = []
        lower_level = []
        for node in nodes:
            if node and node.val:
                level.append(node.val)
                lower_level += [node.left, node.right]

        ret = [level[-1],] if level else []
        if any(x is not None for x in lower_level):
            ret += cls.rightmostOfLevelAndBelow(lower_level)

        return ret

@pytest.mark.parametrize(
    'input_data, expected_output',
    [
        # Test case #1
        (
            # Input
            TreeNode(
                val=1,
                left=TreeNode(
                    val=2,
                    left=None,
                    right=TreeNode(val=5)
                ),
                right=TreeNode(
                    val=3,
                    left=None,
                    right=TreeNode(val=4)
                ),
            ),
            # Expected Output
            [1,3,4],
        ),
        # Test case #2
        (
            # Input
            TreeNode(
                val=1,
                left=TreeNode(
                    val=2,
                    left=TreeNode(
                        val=4,
                        left=TreeNode(val=5),
                        right=None,
                    ),
                    right=None,
                ),
                right=TreeNode(
                    val=3,
                    left=None,
                    right=None,
                ),
            ),
            # Expected Output
            [1,3,4,5],
        ),
        # Test case #3
        (
            # Input
            TreeNode(
                val=1,
                left=None,
                right=TreeNode(
                    val=3,
                    left=None,
                    right=None,
                ),
            ),
            # Expected Output
            [1,3],
        ),
        # Test case #4
        (
            # Input
            TreeNode(),
            # Expected Output
            [],
        ),
    ],
)
def test_case(input_data, expected_output):
    s = Solution()
    result = s.rightSideView(input_data)
    assert expected_output == result
