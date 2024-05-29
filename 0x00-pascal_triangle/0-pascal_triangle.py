#!/usr/bin/python3
"""Define A function to generate Pascal's Triangle"""
import math


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n

    Variables naming:
        - res: Short for result, and will hold
               the elements of the Pascal's Triangle.
        - n: The numbers of rows from Pascal's Triangle.
        - num: Short for number, iteration variable used to hold
               the current row we are calculating.
        - row: Represents the row final value from the triangle.
        - elem: Short for element, iteration variable holding
                the number of propabilities for the current raw.
    """
    res = []
    if n == 0:
        return []
    for num in range(n):
        res.append([])
        res[num].append(1)
        if num > 0:
            for elem in range(1, num):
                res[num].append(res[num - 1][elem - 1] + res[num - 1][elem])
            res[num].append(1)
    return res
