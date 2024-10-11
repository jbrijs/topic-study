from typing import List

'''

Given a list of numbers, find the unique triplets that sum to 0, where i != j != k.

This algorithm uses the two pointer technique to solve the problem. First, sort the input list. This makes the two pointer possible.
Iterate over each value in the list. For each value, set a left pointer at i + 1 and a right pointer at len(input list) - 1.
Check if it is a valid triplet. If yes, add it to the result list. If it is less than 0, then we must increase the sum,
so add 1 to the left pointer. If it is to big, we must decrease our sum by moving the right pointer -1. Add some extra 
conditionals to make sure that we don't count duplicates when you start iterating or when you move the 
left pointer, and the solution is complete.

'''

def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()
        print(nums)
        
        for i, a in enumerate(nums):
            if i > 0 and nums[i - 1] == a:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                three_sum = a + nums[l] + nums[r]
                
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res