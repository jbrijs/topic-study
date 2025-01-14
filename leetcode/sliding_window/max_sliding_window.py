'''
Leetcode #239: Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

This can be solved by using a monotonically decreasing queue.
Basically, the top of the queue must be the max of the current window, so if the top value is less than the new number added in the window, then pop from the front of the queu.
'''

from collections import deque
from typing import List


def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    queue = deque()
    l = r = 0
    res = []

    while r < len(nums):
        while queue and nums[queue[-1]] < nums[r]:
            queue.pop()
            queue.append(r)

            if l > queue[0]:
                queue.popleft()

            if (r + 1) >= k:
                res.append(nums[queue[0]])
                l += 1
            r += 1
