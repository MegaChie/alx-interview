#!/usr/bin/python3
"""
Island perimeter calculator
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
    - grid: A representaion of the island map where water is 0 and land is 1.
    """
    if grid:
        perimeter = 0
        length = len(grid)
        width = len(grid[0])

        for i in range(length):
            for j in range(width):
                if grid[i][j] == 1:
                    # Checks up
                    if i == 0 or grid[i - 1][j] == 0:
                        perimeter += 1
                    # Checks left
                    if j == 0 or grid[i][j - 1] == 0:
                        perimeter += 1
                    # Checks down
                    if i == length - 1 or grid[i + 1][j] == 0:
                        perimeter += 1
                    # Checks right
                    if j == width - 1 or grid[i][j + 1] == 0:
                        perimeter += 1

        return perimeter

    return 0
