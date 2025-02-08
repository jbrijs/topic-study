"""
Leetcode #102: Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""
from typing import List, Optional
from leetcode.trees.invert_tree import TreeNode
from collections import deque

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    if not root:
        return res
    
    queue = deque([(root, 0)])

    while queue:
        node, level = queue.popleft()
        
        if node:
            if level >= len(res):
                res.append([node.val])
            else:
                res[level].append(node.val)
            
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

    return res
    
