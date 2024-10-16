from typing import Optional

'''
Leetcode #226 

Given the root of a binary tree, invert the tree and return its root
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

    if root == None:
        return root

    temp = root.right
    root.right = self.invertTree(root.left)
    root.left = self.invertTree(temp)

    return root
