from typing import List

'''
Leetcode #40: Combination Sum II
Given a collection of candidate numbers (candidates) and a target number 
(target), find all unique combinations in candidates where the candidate 
numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.
'''


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    candidates.sort()

    def dfs(i, curr, total):
        if total == target:
            res.append(curr.copy())
            return
        if total > target or i == len(candidates):
            return

        curr.append(candidates[i])
        dfs(i + 1, curr, total + candidates[i])
        curr.pop()

        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1

        dfs(i + 1, curr, total)
    dfs(0, [], 0)
    return res
