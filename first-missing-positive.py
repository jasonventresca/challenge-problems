#!/usr/bin/env python3
# https://leetcode.com/problems/first-missing-positive/description/

from typing import List

DEBUG = True

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        return 1

    def naive_firstMissingPositive(self, nums: List[int]) -> int:
        if DEBUG: print(f'nums: {nums}')

        positives = [x for x in nums if x > 0]
        sorted_ = list(sorted(positives))
        max_ = max(sorted_)
        for i in range(1, max_ + 1):
            print(i)
            if i not in sorted_:
                return i

        return max_ + 1

def main():
    '''
    Let:
        a = lowest number found in the list, so far
        b = next lowest number "

    Then:
        if a > 1:
            return 1
        elif b - a > 1:
            return a + 1
        else:
            # Bug: What if (b, max_] are all in the list? Then the correct answer would be: max_ + 1.
            return b + 1

    --- TRY AGAIN ---

    Let:
        `m` = lowest number found in the list, so far
        `l` = lowest number found in the list, so far
        `n` = next lowest number which spans a gap from `l`
        `h` = highest number found in the list (i.e. global max)
    '''
    test_cases = [
        (
            [1, 2, 0],
            3,
        ),
        (
            [3, 4, -1, 1],
            2,
        ),
        (
            [7, 8, 9, 11, 12],
            1,
        ),
        (
            [10,   8,       6,      4,      2,      1       3,      5,   7,   9],
           #[10],  [8, 10], [6, 8], [4, 6], [2, 4], [1, 2], [1, 2], ...
        ),
    ]
    s = Solution()
    for (input_, expected_output) in test_cases:
        result = s.firstMissingPositive(input_)
        assert (expected_output == result), \
            f'\nexpected: {expected_output}' \
            f'\n  result: {result}'
    print('All tests passed : )')

if __name__ == '__main__':
    main()
