#!/usr/bin/env python3
# https://leetcode.com/problems/sort-list/
#   difficulty: Medium
#   topics: Divide and Conquer, ...
''' Run with the following commands (replace file name):
    $ pipenv shell
    $ py.test --log-cli-level=debug -v --tb=no sort-list2.py
'''

from typing import List, Optional
import logging
from collections import defaultdict
import math

import pytest

logger = logging.getLogger(__name__)

class ListNode:
    def __init__(self, val: int, nxt: Optional['ListNode'] = None):
        self.val = val
        self.next = nxt

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Implement via MergeSort:
        1.  sortList() is recursive, it takes an input list (i.e. a ListNode to the head of that sub-list).
        2.  Finds the midpoint, divides into two sub-lists.
        3.  Left sub-list must be terminated by setting the rightmost element's .next to null.
        4.  Keep sub-dividing until there's only one element in each sub-list.
        5.  Begin merging (conquer stage) left and right sorted sub-lists (larger one on the right).
        '''
        if not head or head.val is None or head.next is None:
            return head
        logger.debug(f'sortList(): head = {unlink_list(head)}')

        # Find the midpoint
        mid = self.split(head)
        logger.debug(f'mid.val = {mid.val if mid else None}')
        # Sort left and right halves of the split list
        left = self.sortList(head)
        right = self.sortList(mid)
        # Merge the two sorted halves
        return self.merge(left, right)

    def split(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ''' Split the list in half, by walking across it with 2 pointers (at 1x and 2x pace).
            Terminate the first half, by setting its .next to null.
            Return the head of the right half. '''
        logger.debug(f'split(): head.val = {head.val}')
        if not head or head.val is None or head.next is None:
            return head

        dummy = ListNode(0) # dummy head for init
        dummy.next = head
        i1, i2 = dummy, dummy
        while i2 and i2.val is not None and i2.next is not None:
            i1 = i1.next
            i2 = i2.next
            if i2:
                i2 = i2.next

        mid = i1.next
        i1.next = None
        return mid

    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ''' The code is much simpler, cleaner and less bug-prone
            to just create a new 'result' list (dummy head)
            and just append from the next element of either list (the smaller of the two)
            one at a time until both input lists are exhausted. '''
        logger.debug(f'merge(): {unlink_list(list1)}, {unlink_list(list2)}')
        # Set up a dummy head (anchor) and an empty result set to build up from list1 + list2.
        dummyHead = ListNode(0)
        result = dummyHead
        while list1 and list2:
            if list1.val < list2.val:
                logger.debug(f'... {unlink_list(dummyHead)} + {list1.val}')
                result.next = list1
                list1 = list1.next
            else:
                logger.debug(f'... {unlink_list(dummyHead)} + {list2.val}')
                result.next = list2
                list2 = list2.next
            result = result.next

        # Append whatever's left onto the end.
        if list1:
            result.next = list1
        if list2:
            result.next = list2

        logger.debug(f' -> {unlink_list(dummyHead.next)}')
        return dummyHead.next

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
