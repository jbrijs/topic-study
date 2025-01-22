'''
Leetcode #53: Maximum Subarray

Given an integer array nums, find the 
subarray
with the largest sum, and return its sum.

 

Example:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
'''

from typing import List


def maxSubArray(nums: List[int]) -> int:
    max_sum = nums[0]
    curr_sum = nums[0]

    for i in range(1, len(nums)):
        if curr_sum > 0:
            curr_sum += nums[i]
        else:
            curr_sum = nums[i]

        max_sum = max(curr_sum, max_sum)

    return max_sum
