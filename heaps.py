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
