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
        print(f'list: {node_to_list(head)}')
        if DEBUG: print(f'head: {head}')
        return False


def main():
    test_cases = [
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
        assert (expected_output == result), \
            f'\nexpected: {expected_output}' \
            f'\n  result: {result}'
    print('All tests passed : )')

if __name__ == '__main__':
    main()
