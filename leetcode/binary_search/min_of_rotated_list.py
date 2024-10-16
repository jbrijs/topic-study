from typing import List

'''
Leetcode #153 Find Minimum in Rotated Sorted Array

Use binary search but compare mid with end instead of the search parameter
'''


def findMin(self, nums: List[int]) -> int:
        mid = len(nums) // 2
        end = len(nums) - 1



        if nums[mid] > nums[end]:
            print(f"mid: {nums[mid]}, end: {nums[end]}")
            return self.findMin(nums[mid:])
        elif nums[mid] < nums[end]:
            print(f"mid: {nums[mid]}, end: {nums[end]}")
            return self.findMin(nums[:mid +1])
        else:
            print(f"nums: {nums}")
            return min(nums[0], nums[end])
