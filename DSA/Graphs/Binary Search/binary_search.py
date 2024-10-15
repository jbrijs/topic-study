from typing import List, Optional
import unittest


def bs_recursive(input: List[int], find: int) -> Optional[int]:
    mid = len(input) // 2

    if len(input) == 1 and input[mid] != find:
        return None

    elif input[mid] < find:
        return bs_recursive(input[mid + 1:], find)

    elif input[mid] > find:
        return bs_recursive(input[:mid], find)
    else:
        return input[mid]


def bs_iterative(input: List[int], find: int) -> Optional[int]:
    mid = len(input) // 2

    array_slice = input
    while True:
        if len(array_slice) == 1 and array_slice[0] != mid:
            return None
        elif array_slice[mid] > find:
            array_slice = array_slice[:mid]
            mid = len(array_slice) // 2
        elif array_slice[mid] < find:
            array_slice = array_slice[mid + 1:]
            mid = len(array_slice) // 2
        else:
            return array_slice[mid]


class TestBS(unittest.TestCase):
    def test_recursive_1(self):
        answer = bs_recursive([0, 1, 2, 3, 4, 5, 6], 5)
        self.assertEqual(answer, 5)

    def test_recursive_2(self):
        answer = bs_recursive([0, 1, 2, 3, 4, 6], 5)
        self.assertEqual(answer, None)

    def test_recursive_3(self):
        answer = bs_recursive([0, 1, 2, 3], 0)
        self.assertEqual(answer, 0)

    def test_iterative_1(self):
        answer = bs_iterative([0, 1, 2, 3, 4, 5, 6], 5)
        self.assertEqual(answer, 5)

    def test_iterative_2(self):
        answer = bs_iterative([0, 1, 2, 3, 4, 6], 5)
        self.assertEqual(answer, None)

    def test_iterative_3(self):
        answer = bs_iterative([0, 1, 2, 3], 0)
        self.assertEqual(answer, 0)


if __name__ == "__main__":
    unittest.main()
