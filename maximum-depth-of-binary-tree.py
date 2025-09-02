#!/usr/bin/env python3
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#   difficulty: Easy
#   topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
''' Run with the following commands (replace file name):
    $ pipenv shell
    $ py.test --log-cli-level=debug -v --tb=no maximum-depth-of-binary-tree.py
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

def list_to_tree(lst: list) -> TreeNode:
    return TreeNode()

def tree_to_list(root: TreeNode) -> list:
    return list()

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        logger.debug(f'input = {tree_to_list(root)}')
        return 0

@pytest.mark.parametrize(
    'input_data, expected_output',
    [
        # Test case #1
        (
            # Input
            [3,9,20,None,None,15,7],
            # Expected Output
            3,
        ),
        # Test case #2
        (
            # Input
            [1,None,2],
            # Expected Output
            2,
        ),
    ],
)
def test_case(input_data, expected_output):
    s = Solution()
    result = s.maxDepth(list_to_tree(input_data))
    assert expected_output == result
