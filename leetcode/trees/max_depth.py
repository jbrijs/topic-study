from typing import Optional
from leetcode.trees.invert_tree import TreeNode


'''
Leetcode #104

Given the root of a binary tree, return its maximum depth
'''


def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        return max(self.findMaxDepth(root.left, 1), self.findMaxDepth(root.right, 1))

def findMaxDepth(self, root, current_depth):
    if root == None:
        return current_depth
    return max(self.findMaxDepth(root.right, current_depth + 1), self.findMaxDepth(root.left, current_depth + 1))