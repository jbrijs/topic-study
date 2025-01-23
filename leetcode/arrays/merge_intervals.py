'''
Leetcode #55: Merge Intervals:

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

from typing import List


def mergeIntervals(intervals: List[int]) -> List[int]:
    n = len(intervals)
    intervals.sort(key=lambda x: x[0])
    merges = [intervals[0]]

    for i in range(1, n):
        if intervals[i][0] <= merges[-1][1]:
            if intervals[i][1] > merges[-1][1]:
                merges[-1][1] = intervals[i][1]
        else:
            merges.append(intervals[i])

    return merges
