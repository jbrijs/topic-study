'''
Leetcode #435: Non-Overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
'''

from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[1])
    prev = 0
    count = 1

    for i in range(1, len(intervals)):
        if intervals[i][0] >= intervals[prev][1]:
            count += 1
            prev = i
    
    return len(intervals) - count