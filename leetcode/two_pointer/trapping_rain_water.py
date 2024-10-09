from typing import List
'''
LeetCode #42

This algorithm uses the two pointer method do determine how much rainwater
can be stored between blocks of a certain height, represented as an array 
of heights.

We start with a left and right pointer initialized at the start and end
of the heights array, and a max_left and max_right value initialized to
the values at the start and end of the list.

The formula for checking how much rain can be stored at an index of the height array is:
min(max_left, max_right) - height[1]

The amount of rainwater that can be stored at an index is constrained by the minimum 
value of either its left or right block. To get the total amount, we move the side
with the lowest max height. So if max_left <= max_right, we move the left pointer 
one to the right, and vice versa. We then update the max_left variable to be the
max(height[l], max_left). We then used this new max to calculate the amount that
can be stored at the current block, and add this amount to the total. If we updated
the max height after the calculation, we would have to check for negative values
before adding to the total.

The algorithm continues until the left and right pointers meet.

'''


def trap(height: List[int]) -> int:
    l = 0
    r = len(height) - 1
    max_left = height[l]
    max_right = height[r]
    res = 0

    while l < r:
        if max_left < max_right:
            l += 1
            max_left = max(height[l], max_left)
            res += max_left - height[l]
        else:
            r -= 1
            max_right = max(height[r], max_right)
            res += max_right - height[r]

    return res
