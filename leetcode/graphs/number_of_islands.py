from typing import List

'''
Leetcode #200 Number of Islands

Given a mxn binary grid, return the number of islands
'''


def numIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    visited = set()  # [row, col]
    islands = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(row, col):
        stack = [[row, col]]
        while stack:
            node = stack.pop()
            r, c = node
            if (r, c) in visited:
                continue
            else:
                visited.add((r, c))
                if grid[r][c] == "1":
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1":
                            stack.append([nr, nc])

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                dfs(r, c)

    return islands
