#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    pile of coins of different values
    """
    if total <= 0:
        return 0
    dp = [0] + [float("inf")] * (total)
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[-1] if dp[-1] != float("inf") else -1
