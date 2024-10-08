from typing import List
import unittest

'''
LeetCode #238:

Given a list of numbers, return a list of products for each item in the list, where the result is the product of the whole list, excluding that item. Kinda confusing, it makes more sense to look at it.

This can be solved by constructing two arrays, one called 'before' and one 'after'.

In the before array, you calculate the product of the list before that element in the list.
In the after array, you calculate the product of the list after that eleement in the list

Then, you multiply both lists together to get you result list.

'''


def productExceptSelf(nums: List[int]) -> List[int]:
    before = [1 for _ in range(len(nums))]
    after = [1 for _ in range(len(nums))]
    for i in range(1, len(nums)):
        before[i] = nums[i - 1] * before[i - 1]
        i += 1

    for i in range(len(nums) - 2, -1, -1):
        after[i] = nums[i + 1] * after[i + 1]
        i -= 1

    res = []
    for i in range(0, len(nums)):
        res.append(before[i] * after[i])
        i += 1
    return res


class TestProductExceptSelf(unittest.TestCase):
    def test_1(self):
        nums = [1, 2, 3, 4]
        sol = productExceptSelf(nums)
        self.assertEqual(sol, [24, 12, 8, 6])

    def test_2(self):
        nums = [-1, 1, 0, -3, 3]
        sol = productExceptSelf(nums)
        self.assertEqual(sol, [0, 0, 9, 0, 0])


if __name__ == "__main__":
    unittest.main()
