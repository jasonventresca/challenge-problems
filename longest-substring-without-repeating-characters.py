#!/usr/bin/env python3
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#   difficulty: Medium
#   topics: Hash Table, String, Sliding Window

from typing import List

DEBUG = True

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if DEBUG: print(f's = {s}')
        uniq = set()
        max_ht = 0
        curr_s = ''

        for c in s:
            if c in uniq:
                curr_ht = len(curr_s)
                if curr_ht > max_ht:
                    max_ht = curr_ht

                uniq = set()
                curr_s = ''
            else:
                uniq.add(c)
                curr_s += c

        curr_ht = len(curr_s)
        if curr_ht > max_ht:
            max_ht = curr_ht

        return max_ht

def main():
    test_cases = [
        # Test case #1
        (
            # Input
            'abcabcbb',
            # Expected Output
            3,
        ),
        # Test case #2
        (
            # Input
            'bbbbb',
            # Expected Output
            1,
        ),
        # Test case #3
        (
            # Input
            'pwwkew',
            # Expected Output
            3,
        ),
    ]
    s = Solution()
    for (input_, expected_output) in test_cases:
        result = s.lengthOfLongestSubstring(input_)
        assert (expected_output == result), \
            f'\nexpected: {expected_output}' \
            f'\n  result: {result}'
    print('All tests passed : )')

if __name__ == '__main__':
    main()
