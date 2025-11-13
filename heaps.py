#!/usr/bin/env python3

from typing import List
import operator

from icecream import ic

DEBUG = False

class AbstractBaseHeap:
    cmp_heapify_up = None
    cmp_heapify_down = None

    def __init__(self, nums: List[int] = None):
        self.heap = list()
        if not nums:
            return

        for elem in nums:
            self.push(elem)

    def root(self):
        return self.heap[0]

    def parent_of(self, idx: int):
        return (idx - 1) // 2

    def left_child_of(self, idx: int):
        return 2 * idx + 1

    def right_child_of(self, idx: int):
        return 2 * idx + 2

    def push(self, elem: int):
        self.heap.append(elem)
        if DEBUG: print(self.heap)
        idx = len(self.heap) - 1
        self.heapify_up(idx)

    def pop(self):
        if DEBUG: ic('before pop', self.heap)
        prev_root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        if DEBUG: ic('after pop', self.heap)
        return prev_root

    def heapify_down(self, idx: int):
        if DEBUG: ic(self.heap)
        water_mark = idx # low water mark for MinHeap, high for MaxHeap
        size = len(self.heap)
        i = 0

        while True:
            left = self.left_child_of(idx)
            right = self.right_child_of(idx)
            if DEBUG: ic(size, idx, water_mark, left, right)

            if left < size and self.cmp_heapify_down(
                    self.heap[left],
                    self.heap[water_mark]
            ):
                water_mark = left

            if right < size and self.cmp_heapify_down(
                    self.heap[right],
                    self.heap[water_mark]
            ):
                water_mark = right

            if water_mark != idx:
                self.heap[idx], self.heap[water_mark] = \
                    self.heap[water_mark], self.heap[idx]
                idx = water_mark
            else:
                break

    def heapify_up(self, idx: int):
        while idx != 0 and self.cmp_heapify_up(
                self.heap[self.parent_of(idx)],
                self.heap[idx]
        ):
            # swap parent / child
            self.heap[idx], self.heap[self.parent_of(idx)] = \
                self.heap[self.parent_of(idx)], self.heap[idx]
            # move one level up the tree, then reevaluate the while loop
            idx = self.parent_of(idx)

class MinHeap(AbstractBaseHeap):
    cmp_heapify_up = operator.gt
    cmp_heapify_down = operator.lt

class MaxHeap(AbstractBaseHeap):
    cmp_heapify_up = operator.lt
    cmp_heapify_down = operator.gt

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mh = MinHeap()
        if DEBUG: ic(nums)
        for n in nums:
            mh.push(n)
            if len(mh.heap) > k:
                mh.pop()
            if DEBUG: print('---')

        if DEBUG: print("heap:", mh.heap)
        return mh.heap[0]

if __name__ == '__main__':
    test_data = [9,3,5,2,7,6,1,4,5]

    heap = MinHeap(test_data)
    print('min heap:', heap.heap)
    root = heap.root()
    print('root:', root)

    heap = MaxHeap(test_data)
    print('maxheap:', heap.heap)
    root = heap.root()
    print('root:', root)

    sol = Solution()
    assert 5 == sol.findKthLargest([3,2,1,5,6,4], 2)
