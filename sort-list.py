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
        '''
        Implement via MergeSort:
        1.  sortList() is recursive, it takes an input list (i.e. a ListNode to the head of that sub-list).
        2.  Finds the midpoint, divides into two sub-lists.
        3.  Left sub-list must be terminated by setting the rightmost element's .next to null.
        4.  Keep sub-dividing until there's only one element in each sub-list.
        5.  Begin merging (conquer stage) left and right sorted sub-lists (larger one on the right).
        '''
        logger.debug(f'sortList({head.val})')
        if not head or head.next is None:
            return head
        mid = self.split(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def split(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        By stepping forward 2 steps for every one of mid, we reach mid and end at the same time, e.g.
        [   1,   2,   3,   4,   5   ]
           mid
                end
                mid
                          end
                     mid
                               end
        [   1,   2,   3,   4   ]
           mid
                end
                mid
                          end
        [   1,   ]
           mid
           end
        [   1,   2,   ]
           mid
                end
        '''
        if not head or not head.next:
            return head
        mid = head
        end = head
        while end and end.next:
            mid = mid.next
            end = end.next.next
        ret = mid.next
        mid.next = None
        return ret

    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Lists 1 and 2 are each already sorted. We just need to combine them in a sorted order.
        Merge works by creating a new linked list, by appending the smaller of the two leftmost elements of list 1 and list 2, and advancing further into the chosen list.
        As soon as one of the two lists is fully consumed, we can just append the rest of the other list, since it's already sorted within itself, and guaranteed to be larger than the result up to that point.
        '''
        dummyHead = ListNode(0) # set up a head with a dummy node
        result = dummyHead
        while list1 and list2:
            if list1.val < list2.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
        result.next = list1 or list2
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
