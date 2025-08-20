#!/usr/bin/env python3
# https://leetcode.com/??? <-- TODO: Problem URL goes here.
#   difficulty: TODO: difficulty level goes here
#   topics: TODO: topics go here

from typing import List, Optional

DEBUG = False

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'ListNode< val: {self.val}, next =\n  {self.next} >'

def node_to_list(node):
    if node.next is not None:
        return [node.val] + node_to_list(node.next)

    return [node.val]

def list_to_node(list_):
    if len(list_) > 0:
        return ListNode(
            val=list_[0],
            next=list_to_node(list_[1:])
        )

    return None

class Solution:
    def rotateRight(self, head, k):
        '''
        ___PSEUDOCODE___
        If the list is length n, then to rotate it k times can be simplified
        to rotating it (k mod n) times.
        For k < n:
            To rotate k times means the (n - k)th element becomes the tail,
            and the (n - k + 1)th element becomes the head.

        The procedure becomes:
        1. Step through the whole linked list once, i.e. O(n).
        2. Take note of its total length as n.
        3. Compute r = k mod n.
        4. Connect the original tail to the original head (i.e. tail.next = head).
        5. Designate the desired new tail as the (n - r)th element (i.e. new_tail.next = None).
        6. But before you do^, grab a handle to the next element, and later return it (as the new head).
        '''
        print(f'list: {node_to_list(head)}')
        if DEBUG: print(f'head: {head}')

        n = 0
        cur = head
        while cur:
            n += 1
            prev = cur
            cur = cur.next

        r = k % n
        print(f'k: {k}')
        print(f'n: {n}')
        print(f'r: {r}')

        # 4. Connect the original tail to the original head.
        prev.next = head

        # 5.
        cur = head
        for _ in range(n - r):
            cur = head.next
        new_head = cur.next
        cur.next = None

        return new_head


def main():
    test_cases = [
        # Test case #0
        (
            # Input
            ([1,2,3,4,5], 1),
            # Expected Output
            [5,1,2,3,4],
        ),
        # Test case #1
        (
            # Input
            ([1,2,3,4,5], 2),
            # Expected Output
            [4,5,1,2,3],
        ),
    ]
    s = Solution()
    for (input_, expected_output) in test_cases:
        result = s.rotateRight(
            head=list_to_node(input_[0]),
            k=input_[1]
        )
        assert (expected_output == node_to_list(result)), \
            f'\nexpected: {expected_output}' \
            f'\n  result: {node_to_list(result)}'
    print('All tests passed : )')

if __name__ == '__main__':
    main()
