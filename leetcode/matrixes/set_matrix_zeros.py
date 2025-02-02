'''
Leetcode #73: Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
'''

from typing import List


def setZeros(matrix: List[List[int]]) -> None:

    rows = len(matrix)
    cols = len(matrix[0])

    def setRow(row):
        for c in range(cols):
            matrix[row][c] = 0

    def setCol(col):
        for r in range(rows):
            matrix[r][cols] = 0

    zeros = []
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                zeros.append((r, c))

    while zeros:
        row, col = zeros.pop()
        setRow(row)
        setCol(col)

    return matrix