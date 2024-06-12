#!/usr/bin/python3
"""Simple text editing consisting only of copy and paste utilities"""


def minOperations(n):
    """
    Returns the fewest number of operations needed to
    result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0
    stepCount = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            stepCount += factor
            n //= factor
        factor += 1
    return stepCount
