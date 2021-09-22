#!/usr/bin/env python3

import pprint
import unittest


DEBUG = False

def list_contains_sum(l, k):
    def get_power_set(iterable_):
        pset = set()

        for x in l:
            for y in frozenset(pset):
                pset.add(y + x)

            pset.add(x)

        if DEBUG:
            pprint.pprint(list(sorted(pset)))

        return pset

    all_sums = get_power_set(k)
    return k in all_sums


class TestContainsSum(unittest.TestCase):
    def test_present(self):
        self.assertTrue(
            list_contains_sum(
                l = [10, 15, 3, 7],
                k = 17
            )
        )

    def test_missing(self):
        self.assertFalse(
            list_contains_sum(
                l = [10, 15, 3, 7],
                k = 19
            )
        )

    def test_negative(self):
        self.assertTrue(
            list_contains_sum(
                l = [5, 4, 3, -1],
                k = -1
            )
        )

    def test_negative_pair(self):
        self.assertTrue(
            list_contains_sum(
                l = [5, 4, 3, -1],
                k = 2
            )
        )

    def test_empty(self):
        self.assertFalse(
            list_contains_sum(
                l = [],
                k = 1
            )
        )

if __name__ == '__main__':
    unittest.main(verbosity=2)
