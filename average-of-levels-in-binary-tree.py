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

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        logger.debug(f'root: {root}')
        return False

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
