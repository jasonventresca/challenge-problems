#!/usr/bin/env python3

from typing import List
import operator

DEBUG = False

def solution(coins: List[int], amount: int) -> int:
    return 0

def main():
    test_data = [
        { 'coins': [1,2], 'amount': 3, 'answer': 2 },
    ]

    for td in test_data:
        obs = solution(td['coins'], td['amount'])
        exp = td['answer']
        assert exp == obs, \
            f'Expected: {exp} != Observed: {obs}'

if __name__ == '__main__':
    main()
