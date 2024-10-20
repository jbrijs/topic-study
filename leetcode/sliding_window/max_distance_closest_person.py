from typing import List

'''
Leetcode #849 - Maximum distance to closest person

You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.
'''


def maxDistToClosest(seats: List[int]) -> int:
        max_dist = 0
        n = len(seats)

        # Handle leading empty seats
        l = 0
        while seats[l] == 0:
            l += 1
        max_dist = max(max_dist, l)
        
        # Handle the seats between occupied ones
        prev = l
        for i in range(l + 1, n):
            if seats[i] == 1:
                max_dist = max(max_dist, (i - prev) // 2)
                prev = i
        
        # Handle trailing empty seats
        if seats[-1] == 0:
            max_dist = max(max_dist, n - 1 - prev)
        
        return max_dist