from typing import List

'''
Leetcode #853

There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
You are given two integer array position and speed, both of length n, where position[i] is the starting
mile of the ith car and speed[i] is the speed of the ith car in miles per hour. A car cannot pass another 
car, but it can catch up and then travel next to it at the speed of the slower car. A car fleet is a
car or cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.
If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.
Return the number of car fleets that will arrive at the destination.

We can solve this using a stack. If we look at the cars as a combined and reversed array of position 
and speed, and then check the time that it will reach the target, add that time to the stack, and pop 
any duplicates and anything greater, whats left on the stack will be thte number of car fleets

'''


def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    pairs = [[p, s] for p, s in zip(position, speed)]

    stack = []
    for p, s in sorted(pairs)[::-1]:
        time = (target - p) / s
        stack.append(time)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)
