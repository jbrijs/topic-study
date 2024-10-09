from typing import List

'''
LeetCode #347

Given a list of numbers and a number 'k', find the kth most frequently occuring numbers.

To solve this, first we iterate through the list, and add the occurences for each number
into a map where the key is the number and the value is the value of occurences. Then a
2D array is initialized. Iterating through the key value pairs of the map, add the key 
to the list at index == occurences in the 2D array. Next, iterate backwards through the
array and append the values to the result list. Once the lenght of the result list == k,
 return the result list.
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        res = []

        for num in nums:
            map[num] = map.get(num, 0) + 1

        for key, value in map.items():
            buckets[value].append(key)

        for i in range(len(buckets) - 1, 0, -1):
            for val in buckets[i]:
                res.append(val)
                if len(res) == k:
                    return res

      