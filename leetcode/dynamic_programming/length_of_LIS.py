from typing import List

'''
Leetcode #300. Longest Increasing Subsequence
Given an integer array nums, return the length of the longest strictly increasing 
subsequence.
'''

def lengthOfLIS(nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)