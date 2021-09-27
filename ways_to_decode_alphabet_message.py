#!/usr/bin/env python3

import unittest
import logging

"""
Daily Coding Problem / Inbox Problem #7 / Medium Difficulty

Given the mapping a=1, b=2, ... z=26, and an encoded message,
count the number of ways it can be decoded.

For example, the message "111" would give 3,
since it could be decoded as "aaa", "ka", and "ak".

You can assume that the messages are decodable.
For example, "001" is not allowed.
"""


def decode_message(n: int) -> int:
    return 0


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

        example 1:   111     ->  3   // aaa , ka , ak
            - 1=a   1=a     1=a
            - 11=k  1=a
            - 1=a   11=k

        example 2   26      ->  2   // bf , z
            - 2=b   6=f
            - 26=z

        example 3   101     ->  1   // ja
            - 10=j  1=a
            ! 1=a   0=Exception()   1=a
            ! 1=a   01=Exception()

        example 4   110     ->  1   // aj
            - 1=a   10=j
            ! 11=k  0=Exception()
    """

    # TODO - rename test case method names
    def test_1(self):
        self.assertEqual(decode_message(111), 3)

    def test_2(self):
        self.assertEqual(decode_message(26), 2)

    def test_3(self):
        self.assertEqual(decode_message(101), 1)

    def test_4(self):
        self.assertEqual(decode_message(110), 1)


    def test_case_one(self):
        self.assertEqual(1, True)

        with self.assertRaises(KeyError):
            raise KeyError()

        return


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    ROOT_LOGGER = logging.getLogger()

    for x in range(1, 26 + 1):
        ROOT_LOGGER.debug("{}\t->\t{}".format(
            x,
            _decode_single_char(x)
        ))

    unittest.main(verbosity=2)
