'''
Leetcode #54: Spiral Matrix:

Given an m x n matrix, return all elements of the matrix in spiral order.
'''

from typing import List


def spiralOrder(matrix: List[List[int]]):
    
    rows = len(matrix)
    cols = len(matrix[0])
    visited = set()
    res = []
    curr = 0
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    r, c = 0

    while len(visited) < rows * cols:
        visited.add((r, c))
        res.append(matrix[r][c])

        next_r = r + d[curr][0]
        next_c = c + d[curr][0]

        if next_r < 0 or next_r == rows or next_c < 0 or next_c == 0 or (next_r, next_c) in visited:
            curr = (curr + 1) % 4
            next_r = r + d[curr][0]
            next_c = c + d[curr][0]
        
        r, c = next_r, next_c

    return res