"""
Leetcode # : Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's 
in the binary representation of i.
"""

from typing import List


def countBits(n: int) -> List[int]:
    dp = [0] * (n + 1)
    sub = 1

    for i in range(1, n + 1):
        if sub * 2 == i:
            sub = i

        dp[i] = dp[i - sub] + 1
    
    return dp