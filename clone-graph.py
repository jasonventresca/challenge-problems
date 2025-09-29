#!/usr/bin/env python3
# https://leetcode.com/problems/clone-graph
#   difficulty: Medium
#   topics: Hash Table, Depth-First Search, Breadth-First Search, Graph
''' Run with the following commands (replace file name):
    $ pipenv shell
    $ py.test --log-cli-level=debug -v --tb=no clone-graph.py
'''

from typing import List, Optional
import logging
from collections import defaultdict
import math

import pytest
from icecream import ic

logger = logging.getLogger(__name__)

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        logger.debug(f'node: {node}')
        edges = set()
        self.explore(node, edges)
        print(f'edges: {list(sorted(edges))}')

    @classmethod
    def explore(cls, node, edges):
        for nb in node.neighbors:
            this_edge = tuple(sorted([node.val, nb.val]))
            if this_edge not in edges:
                edges.add(this_edge)
                cls.explore(nb, edges)

IO_1 = Node(
    val=1,
    neighbors=[
        Node(
            val=2,
            neighbors=[
                Node(
                    val=1,
                ),
                Node(
                    val=3,
                ),
            ],
        ),
        Node(
            val=4,
            neighbors=[
                Node(
                    val=1,
                ),
                Node(
                    val=3,
                ),
            ],
        ),
    ],
)

@pytest.mark.parametrize(
    'input_data, expected_output',
    [
        # Test case #1
        (
            # Input
            IO_1,
            # Expected Output
            IO_1,
        ),
    ],
)
def test_case(input_data, expected_output):
    s = Solution()
    result = s.cloneGraph(input_data)
    assert expected_output == result
