'''
Leetcode #152: Maximum Product Subarray

Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.
'''

from typing import List


def maxProduct(nums: List[int]) -> int:
    if not nums:
        return 0

    max_prod, min_prod, res = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(nums[i], max_prod * nums[i])
        min_prod = max(nums[i], min_prod * nums[i])

        res = max(max_prod, res)

    return res
