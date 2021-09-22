#!/usr/bin/env python3

import unittest
import pprint

DEBUG = True

COUNTER = 0

def get_manhattan_distance(grid, home_xy, park_xy):
    """ :grid: an NxN list of strings where each character is either a park 'P', home 'H', or empty ' '
        :home_xy: the (x,y) coordinates (expressed as a list) of the source home
        :park_xy: the (x,y) coordinates (expressed as a list) of the destination park

        brief: Return the minimum distance (as an integer) one must walk from the home to the park.
               Note that residents cannot walk or swim through water; they must walk aruond.
    """
    global COUNTER
    COUNTER += 1

    return COUNTER


def plan_city(grid, parks):
    homes = []
    empties = []
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == 'H':
                homes.append([x, y])
            elif cell == ' ':
                empties.append([x, y])

    # mapping of park coordinates to their total walking distance
    park_distances = []

    for empty in empties:
        # try putting a park in this empty spot
        park = empty

        # see how far everyone would have to walk to this park
        total_distance = 0
        for home in homes:
            total_distance += get_manhattan_distance(grid, home, park)

        park_distances.append([park, total_distance])

    park_distances_sorted = sorted(park_distances, key=lambda x: x[1])
    best_parks = [x[0] for x in park_distances_sorted[:parks]]

    # don't mutate the original grid - copy into a new list
    output_grid = list(grid)

    # fill the parks into the grid
    for park_xy in best_parks:
        as_list = list(output_grid[x])
        as_list[y] = 'P'
        output_grid[x] = ''.join(as_list)

    return output_grid

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
