from typing import List

'''
Leetcode #695

Given an mxn binary grid, find the maximum area of an island. An island is any value with a 1 that has optional connections in its 4 directions

Use DFS to find the area of an island once one is found
'''


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    visited = set()  # (row, col)
    res = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 0:
                visited.add((row, col))
            else:
                if (row, col) not in visited:
                    stack = [(row, col)]
                    island = 0
                    while stack:
                        r, c = stack.pop()
                        if (r, c) not in visited:
                            visited.add((r, c))
                            island += 1
                            if r - 1 >= 0 and grid[r - 1][c] == 1 and (r-1, c) not in visited:
                                stack.append((r - 1, c))
                            if r + 1 < len(grid) and grid[r + 1][c] == 1 and (r+1, c) not in visited:
                                stack.append((r + 1, c))
                            if c - 1 >= 0 and (r, c-1) not in visited and grid[r][c - 1] == 1:
                                stack.append((r, c - 1))
                            if c + 1 < len(grid[0]) and grid[r][c + 1] == 1 and (r, c+1) not in visited:
                                stack.append((r, c + 1))

                    res = max(island, res)

    return res
