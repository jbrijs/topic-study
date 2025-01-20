from typing import List

'''
Leetcode #268: Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''


def missingNumber(self, nums: List[int]) -> int:
    res = [-1] * (len(nums) + 1)

    for num in nums:
        res[num] = num

    for i in range(len(res)):
        if res[i] == -1:
            return i
