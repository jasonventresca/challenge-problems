#!/usr/bin/env python3

import unittest
import pprint

DEBUG = 1


def get_manhattan_distance(grid, home_xy, park_xy):
    """ :grid: an NxN list of strings where each character is either a park 'P', home 'H', or empty ' '
        :home_xy: the (x,y) coordinates (expressed as a list) of the source home
        :park_xy: the (x,y) coordinates (expressed as a list) of the destination park

        brief: Return the minimum distance (as an integer) one must walk from the home to the park.
               Note that residents cannot walk or swim through water; they must walk aruond.
    """

    # naive approach: assume residents can walk/swim through water
    distance = abs(home_xy[0] - park_xy[0]) + abs(home_xy[1] - park_xy[1])

    if DEBUG >= 2:
        print("H: ({},{}) , P: ({},{}) , D = {}".format(
            *home_xy, *park_xy, distance
        ))

    return distance


def plan_city(grid, parks):
    # so the first line of actual debug printing is not on the same line as the unittest output
    if DEBUG >= 1:
        print("")

    # scan the grid for homes and empty spaces
    homes = []
    empties = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'H':
                homes.append([x, y])
            elif cell == ' ':
                empties.append([x, y])

    # initialize a mapping of park coordinates to their total walking distance
    park_distances = []

    # consider putting a park in each empty space.
    # compute the manhattan distances for all home residents and record that along with the prospective park location.
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

    if DEBUG >= 1:
        print("park locations, sorted from best to worst:")
        for i, park_distance in enumerate(park_distances_sorted):
            park, distance = park_distance
            print("park #{}: location = {}, distance = {}".format(i + 1, park, distance))

    # don't mutate the original grid - copy into a new list
    output_grid = list(grid)

    # fill the parks into the grid
    for park_xy in best_parks:
        x, y = park_xy
        as_list = list(output_grid[y])
        as_list[y] = 'P'
        output_grid[y] = ''.join(as_list)

    return output_grid


def _print_grid(grid):
    if not grid:
        return

    width = len(grid[0])
    print("+" + "-" * width + "+")
    for row in grid:
        print("|" + row + "|")
    print("+" + "-" * width + "+")


class TestMinimizeParksHomesDistance(unittest.TestCase):
    def _base_test(self, observed, expected):
        if DEBUG >= 1:
            print("observed:")
            _print_grid(observed)
            print("expected:")
            _print_grid(expected)

        self.assertEqual(observed, expected)

    def test_small(self):
        observed = plan_city(
            grid = [
                "   H ",
                " W W ",
                "H    ",
            ],
            parks = 1,
        )
        expected = [
            "   H ",
            " WPW ",
            "H    ",
        ]
        self._base_test(observed, expected)

    def test_big(self):
        observed = plan_city(
            grid = [
                "   H    H",
                " W  WHW  ",
                "H    W   ",
            ],
            parks = 1,
        )
        expected = [
            "   H ",
            " WPW ",
            "H    ",
        ]
        self._base_test(observed, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
