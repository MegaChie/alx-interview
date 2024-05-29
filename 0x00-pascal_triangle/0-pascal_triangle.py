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
        - elem: Short for element, iteration variable holding
                the calculation for the current raw's elements.
    """
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            res.append(level)
    return res
