#!/usr/bin/env python3

from typing import List
import operator

class AbstractBaseHeap:
    cmp = None

    def __init__(self, nums: List[int]):
        self.heap = list()
        for elem in nums:
            self.insert(elem)

    def insert(self, elem: int):
        self.heap.append(elem)
        idx = len(self.heap) - 1
        self.heapify_up(idx)

    def parent_of(self, idx: int):
        return (idx - 1) // 2

    def heapify_up(self, idx: int):
        while idx != 0 and self.cmp(self.heap[self.parent_of(idx)], self.heap[idx]):
            # swap parent / child
            self.heap[idx], self.heap[self.parent_of(idx)] = \
                self.heap[self.parent_of(idx)], self.heap[idx]
            # move one level up the tree, then reevaluate the while loop
            idx = self.parent_of(idx)

    def root(self):
        return self.heap[0]

class MinHeap(AbstractBaseHeap):
    cmp = operator.gt

class MaxHeap(AbstractBaseHeap):
    cmp = operator.lt

class MinHeap:
    def __init__(self, nums: List[int] = None):
        self.heap = list()
        if not nums:
            return

        for elem in nums:
            self.push(elem)

    def push(self, elem: int):
        self.heap.append(elem)
        idx = len(self.heap) - 1
        self.heapify_up(idx)

    def pop(self):
        prev_root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return prev_root

    def parent_of(self, idx: int):
        return (idx - 1) // 2

    def left_child_of(self, idx: int):
        return 2 * idx + 1

    def right_child_of(self, idx: int):
        return 2 * idx + 2

    def heapify_down(self, idx: int):
        largest = idx
        size = len(self.heap)

        while True:
            left = self.left_child_of(idx)
            right = self.right_child_of(idx)

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right
            if largest != idx:
                self.heap[idx], self.heap[largest] = \
                    self.heap[largest], self.heap[idx]
            else:
                break

    def heapify_up(self, idx: int):
        while idx != 0 and self.heap[self.parent_of(idx)] > self.heap[idx]:
            # swap parent / child
            self.heap[idx], self.heap[self.parent_of(idx)] = \
                self.heap[self.parent_of(idx)], self.heap[idx]
            # move one level up the tree, then reevaluate the while loop
            idx = self.parent_of(idx)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mh = MinHeap()
        for n in nums:
            mh.push(n)
            if len(mh.heap) > k:
                mh.pop()

        print("heap:", mh.heap)
        return mh.heap[0]

if __name__ == '__main__':
    test_data = [9,3,5,2,7,6,1,4,5]

    #heap = MinHeap(test_data)
    #print('min heap:', heap.heap)
    #root = heap.root()
    #print('root:', root)

    heap = MaxHeap(test_data)
    print('maxheap:', heap.heap)
    root = heap.root()
    print('root:', root)

    sol = Solution()
    sol.findKthLargest([3,2,1,5,6,4], 2)
