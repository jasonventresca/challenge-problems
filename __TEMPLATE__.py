#!/usr/bin/env python3
# https://leetcode.com/??? <-- TODO: Problem URL goes here.

DEBUG = True

class Solution:
    def problem(self, input_): # TODO: Paste leetcode-provided method here.
        if DEBUG: print(f'problem(): input_ = {input_}')
        return False

def main():
    test_cases = [
        # Test case #1
        (
            # Input
            'foo',
            # Expected Output
            'bar',
        ),
    ]
    s = Solution()
    for (input_, expected_output) in test_cases:
        result = s.problem(input_)
        assert (expected_output == result), \
            f'\nexpected: {expected_output}' \
            f'\n  result: {result}'
    print('All tests passed : )')

if __name__ == '__main__':
    main()
