from typing import List

'''
LeetCode #347
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

      