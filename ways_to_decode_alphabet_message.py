#!/usr/bin/env python3

import unittest

"""
Daily Coding Problem / Inbox Problem #7 / Medium Difficulty

Given the mapping a=1, b=2, ... z=26, and an encoded message,
count the number of ways it can be decoded.

For example, the message "111" would give 3,
since it could be decoded as "aaa", "ka", and "ak".

You can assume that the messages are decodable.
For example, "001" is not allowed.
"""


def _decode_single_char(n: int) -> str:
    error_message = "n must be an integer from 1 to 26"
    assert type(n) == int, error_message
    assert 1 <= n <= 26, error_message

    # chr(97) == 'a'
    # chr(97 + 25) == 'z'
    return chr(n + 96)


class TestCaseOne(unittest.TestCase):
    """
        mapping
            1   a
            2   b
            ...
            26  z
        simple_1:   111     ->  3   // aaa , ka , ak
    """


    def test_case_one(self):
        self.assertEqual(1, True)

        with self.assertRaises(KeyError):
            raise KeyError()

        return


if __name__ == "__main__":
    for x in range(1, 26 + 1):
        print("{}\t->\t{}".format(
            x,
            _decode_single_char(x)
        ))

    unittest.main()
