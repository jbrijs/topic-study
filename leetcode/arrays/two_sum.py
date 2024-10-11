from typing import List

'''
Given a list of numbers and a target value,
return the indices of the two numbers that 
add up to the target, assuming a unique solution
'''

def twoSum(nums: List[int], target: int) -> List[int]:
    value_index_map = {}
    for i, num in enumerate(nums):
        remaining = target - num
        if remaining in value_index_map:
            return [value_index_map[remaining], i]
        value_index_map[num] = i
