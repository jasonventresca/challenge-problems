#!/usr/bin/env python3

import unittest
import pprint

DEBUG = True

def plan_city(grid, parks):
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            pass

    return []

class TestMinimizeParksHomesDistance(unittest.TestCase):
    def test_one(self):
        self.assertEqual(
            plan_city(
                grid = [
                    "   H ",
                    " W W ",
                    "H    ",
                ],
                parks = 1,
            ),
            [
                "   H ",
                " WPW ",
                "H    ",
            ]
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)
