#!/usr/bin/python3
"""
A classic problem from the domain of dynamic programming and greedy algorithms
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet a given amount total,
    or returns -1 if it is not possible to do so.
    """
    if total == 0:
        return 0
    if not coins or len(coins) == 0:
        return -1

    dp = [float("inf")] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float("inf"):
        return -1
    return dp[total]
