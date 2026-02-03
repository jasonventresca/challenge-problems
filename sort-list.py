#!/usr/bin/env python3
# https://leetcode.com/problems/sort-list/
#   difficulty: Medium
#   topics: Divide and Conquer, ...
''' Run with the following commands (replace file name):
    $ pipenv shell
    $ py.test --log-cli-level=debug -v --tb=no sort-list.py
'''

from typing import List, Optional
import logging
from collections import defaultdict
import math

import pytest
from icecream import ic

logger = logging.getLogger(__name__)

class ListNode:
    def __init__(self, val: int, nxt: Optional['ListNode'] = None):
        self.val = val
        self.next = nxt

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return False

def link_list(lst: List) -> ListNode:
    nxt = None
    for item in reversed(lst):
        ln = ListNode(item)
        if nxt is not None:
            ln.next = nxt
        nxt = ln
    return ln

def unlink_list(head: ListNode) -> List:
    ret = []
    while head:
        ret.append(head.val)
        head = head.next
    return ret

@pytest.mark.parametrize(
    'input_data, expected_output',
    [
        # Test case #1
        (
            # Input
            [10, 1, 60, 30, 5],
            # Expected Output
            [1, 5, 10, 30, 60],
        ),
    ],
)
def test_case(input_data, expected_output):
    s = Solution()
    logger.debug(f'input: {input_data}')
    result = s.sortList(link_list(input_data))
    assert expected_output == unlink_list(result)
