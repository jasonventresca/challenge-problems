#!/usr/bin/env python3

import unittest
import logging
import typing
import pprint

"""
Daily Coding Problem / Inbox Problem #7 / Medium Difficulty

Given the mapping a=1, b=2, ... z=26, and an encoded message,
count the number of ways it can be decoded.

For example, the message "111" would give 3,
since it could be decoded as "aaa", "ka", and "ak".

You can assume that the messages are decodable.
For example, "001" is not allowed.
"""

class NotEnoughCharsToDecodeMulti(Exception):
    pass


def _get_all_valid_decodings(n: int) -> typing.Set[str]:
    """
        :param n:   integer from 1 to 26, representing the encoded message
        :returns:   set of strings, representing the set of valid decodings as strings
    """

    digits = tuple([int(x) for x in str(n)])
    ret = set()
    prev = None
    past_2_digits = None
    message = ""
    message_valid = True
    for i, d in enumerate(digits):
        ROOT_LOGGER.debug("evaluating: '{}'".format(d))

        try:
            decoded_single = _decode_single_char(d)
            message += decoded_single

        except:
            # TODO: Catch a custom (or otherwise adequately specific) exception to mitigate against a potential bug in reacting to the wrong exception.

            # The exception was either due to attempting to decode a zero,
            # or an otherwise invalid character (represented numerically).
            message_valid = False

        try:
            if not prev:
                raise NotEnoughCharsToDecodeMulti()

            ROOT_LOGGER.debug("d='{}', prev='{}'".format(d, prev))
            past_2_digits = int("{}{}".format(prev, d))
            decoded_multi = _decode_single_char(past_2_digits)
            # The past two digits can be interpreted
            # as a valid, single character.
            # Branch off to any new messages that can be
            # merged into our final result set.
            head = message[:-2] + decoded_multi
            if i < len(digits) - 1:
                numeric_tail = int("".join([str(x) for x in digits[i+1:]]))
                tails_set = _get_all_valid_decodings(numeric_tail)
                for tail in tails_set:
                    ROOT_LOGGER.debug("adding head = {} , tail = {}".format(head, tail))
                    ret.add(head + tail)
            else:
                # TODO: Comment to explain here.
                ROOT_LOGGER.debug("adding head = {}".format(head))
                ret.add(head)

        except NotEnoughCharsToDecodeMulti as e:
            pass

        except Exception as e:
            # TODO: Catch a custom (or otherwise adequately specific) exception to mitigate against a potential bug in reacting to the wrong exception.
            ROOT_LOGGER.warning(e)
            message_valid = False

        prev = d

    if message_valid:
        ROOT_LOGGER.debug("adding accumulated message: {}".format(message))
        ret.add(message)

    return ret


def count_valid_decodings(n: int) -> int:
    """
        :param n:   integer from 1 to 26 representing the encoded message
        :returns:   positive integer, the total number of valid messages that can be decoded from the input message
    """
    print()
    print("test case: n = {}".format(n))

    try:
        res = _get_all_valid_decodings(n)
        ROOT_LOGGER.debug("count_valid_decodings(): res =\n{}".format(
            pprint.pformat(res)
        ))
        return len(res)
    except:
        ROOT_LOGGER.exception("count_valid_decodings(): fatal exception")
        return 0


def _decode_single_char(n: int) -> str:
    error_message = "n must be an integer from 1 to 26: n had value {}, type {}".format(n, type(n))
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
        self.assertEqual(count_valid_decodings(111), 3) # aaa , ka , ak

    def test_2(self):
        self.assertEqual(count_valid_decodings(26), 2) # bf , z

    def test_3(self):
        self.assertEqual(count_valid_decodings(101), 1) # ja

    def test_4(self):
        self.assertEqual(count_valid_decodings(110), 1) # aj

    def test_5(self):
        self.assertEqual(count_valid_decodings(11), 2) # aa , k

    def test_6(self):
        self.assertEqual(count_valid_decodings(110101), 1) # ajja


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    ROOT_LOGGER = logging.getLogger()

    for x in range(1, 26 + 1):
        ROOT_LOGGER.debug("{}\t->\t{}".format(
            x,
            _decode_single_char(x)
        ))

    unittest.main(verbosity=2)
