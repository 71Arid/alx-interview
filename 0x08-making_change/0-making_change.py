#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins
needed to meet a given amount total.
"""


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total"""
    dp = [total + 1] * (total + 1)
    dp[0] = 0
    for i in range(1, total + 1):
        for j in range(len(coins)):
            dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    return -1 if dp[total] > total else dp[total]
