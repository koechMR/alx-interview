#!/usr/bin/python3
"""
0-island_perimeter
"""


def island_perimeter(grid):
    """ Returns perimeter of an island. """
    perimeter = 0
    w = len(grid)
    p = len(grid[0])

    for q in range(w):
        for e in range(p):
            if grid[q][e] == 1:
                for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    a, b = q + x, e + y
                    # print(a, b)
                    if a >= w or b >= p or a < 0 or b < 0 or grid[a][b] == 0:
                        perimeter += 1
    return perimeter
