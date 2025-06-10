#!/usr/bin/env python3
# https://leetcode.com/problems/group-anagrams/

from typing import List
from collections import defaultdict
import json
from pprint import pprint

DEBUG = False

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs or not any(strs):
            return [['']]

        uniques = defaultdict(list)
        for s in strs:
            ordered = ''.join(sorted(s))
            if DEBUG: print(f's: {s}')
            if DEBUG: print(f'o: {ordered}')
            if DEBUG: print()
            uniques[ordered].append(s)

        if DEBUG: pprint(uniques, indent=4)

        return list(uniques.values())


def _custom_sort(data):
    return list(sorted(
        [
            list(sorted(x))
            for x in data
        ]
    ))

def main():
    test_cases = [
        (
            ['eat','tea','tan','ate','nat','bat'],
            [['bat'],['nat','tan'],['ate','eat','tea']],
        ),
        (
            [''],
            [['']],
        ),
        (
            ['a'],
            [['a']],
        ),
    ]
    s = Solution()
    for (input_, expected_output) in test_cases:
        result = s.groupAnagrams(input_)
        sorted_result = _custom_sort(result)
        sorted_expected_output = _custom_sort(expected_output)
        assert (sorted_expected_output == sorted_result), \
            f'\nexpected: {sorted_expected_output}' \
            f'\n  result: {sorted_result}'
    print('All tests passed : )')

if __name__ == '__main__':
    main()
