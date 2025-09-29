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
        return self.constructFromEdges(edges)

    @classmethod
    def explore(cls, node, edges):
        for nb in node.neighbors:
            this_edge = tuple(sorted([node.val, nb.val]))
            if this_edge not in edges:
                edges.add(this_edge)
                cls.explore(nb, edges)

    @classmethod
    def constructFromEdges(cls, edges):
        '''
        ### Phase 1 ###
        Iterate through list of edges.
        Create or enrich the two nodes joined by the edge.
        Enrichment consists of adding the neighbor to the node's list of neighbors.
        Nodes are tracked in a hashmap, indexed by the node's value.
        ### Phase 2 ###
        Set node = the first node.
        Iterate through the hashmap.
        For each node in the hashmap,
        Replace each of its neighbors with the Node object from the hashmap.
        '''
        ### Phase 1 ###
        nodes = dict()
        for e in sorted(edges):
            both = (
                e,
                tuple(reversed(e)),
            )
            for b in both:
                to, from_ = b
                if from_ not in nodes:
                    nodes[from_] = Node(val=from_)

                if to not in nodes[from_].neighbors:
                    nodes[from_].neighbors.append(to)

        ### Phase 2 ###
        node = nodes.get(1)
        for k, v in nodes.items():
            neighbor_vals = nodes[k].neighbors
            neighbor_nodes = [nodes[x] for x in neighbor_vals]
            nodes[k].neighbors = neighbor_nodes

        return node

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
