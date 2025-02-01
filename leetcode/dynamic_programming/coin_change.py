"""
Leetcode #322: Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""

from typing import List


def coinChange(coins: List[int], amount: int) -> int:

    if amount == 0:
        return 0

    memo = [[float("inf") for _ in range(len(coins))] for _ in range(amount + 1)]

    for i in range(len(coins)):
        memo[i][0] == ()

    for i in range(len(coins)):
        for j in range(1, amount + 1):
            memo[i][j] = memo[i - 1][j] if i > 0 else float("inf")

            if j >= coins[i]:
                memo[i][j] = min(memo[i][j], 1 + memo[i][j - coins[i]])

    result = memo[len(coins) - 1][amount]

    return result if result != float("inf") else -1
