from typing import List

'''
Leetcode #739

Given an a list of temperatures, return a list answer such that answer[i] is the number of days it took to find a higher temp.

This can be brute forced in O(n^2) time with two-pointers, but can be done in O(n) time with O(n) memory.

Initilaize a result array with all 0s
Create an empty stack. The stack will hold [temp, index]
Iterate through each temperature. If the temp is lower than
the temp on the top of the stack, add that temp/index to the 
stack. If it is greater, pop the stack and update the res array.
Continue while this temp is higher than the top of the stack, and 
then add it to the stack.
'''


def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

    res = [0 for _ in range(len(temperatures))]
    stack = []  # [temp, index]

    for i, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            stack_temp, stack_i = stack.pop()
            res[stack_i] = i - stack_i
        stack.append([temp, i])

    return res
