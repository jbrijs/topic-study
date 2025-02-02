"""
Leetcode #207: Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

from typing import List
from collections import deque


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    adj = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    ans = []

    for p in prerequisites:
        course = p[0]
        prereq = p[1]
        adj[prereq] = course
        indegree[course] += 1

    queue = deque()
    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        ans.append(node)

        for next_node in adj[node]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(node)

    return len(ans) == numCourses
