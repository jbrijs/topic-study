'''
Leetcode #417: Pacific Atlantic Water Flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. 
You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at 
coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, 
and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell 
adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell 
(ri, ci) to both the Pacific and Atlantic oceans.
'''

from typing import List


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    rows, cols = len(heights), len(heights[0])

    pacific = [[False] * cols for _ in range(rows)]
    atlantic = [[False] * cols for _ in range(rows)]

    def dfs(r, c, visited, prev_height):
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or heights[r][c] < prev_height:
            return
        visited[r][c] = True
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for dr, dc in directions:
            dfs(dr + r, dc + c, visited, heights[r][c])

    for i in range(rows):
        dfs(i, 0, pacific, heights[i][0])
        dfs(i, cols - 1, atlantic, heights[i][cols - 1])

    for j in range(cols):
        dfs(0, j, atlantic, heights[0][j])
        dfs(rows - 1, j, pacific, heights[rows - 1][j])

    res = []
    for i in range(rows):
        for j in range(cols):
            if atlantic[i][j] and pacific[i][j]:
                res.append([i, j])
    
    return res
