'''
Leetcode #39: Combination Sum

Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 
combinations for the given input.
'''

from typing import List


def combinationSum(candidates: List[int], target: int) -> List[int]:

    res = []
    candidates.sort()

    def dfs(start, sol, sum):

        if sum == target:
            res.append(sol)
            return

        if sum > target:
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            dfs(i, sol + [candidates[i]], sum + candidates[i])

    return res