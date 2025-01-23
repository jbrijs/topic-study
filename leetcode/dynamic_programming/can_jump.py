'''
Leetcode #55: Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
'''

from typing import List


def canJump(nums: List[int]):
    n = len(nums)
    target = n - 1

    def backtrack(curr, target):
        if curr < 0:
            return target == 0
        if curr + nums[curr] >= target:
            target = curr
        backtrack(curr - 1, target)
    
    return backtrack(n - 1, target)