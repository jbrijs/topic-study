'''
Leetcode #100: Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def checkTree(p, q):
        if p and q:
            if p.val == q.val:
                return checkTree(p.left, q.left) and checkTree(p.right, q.right)
            else:
                return False
        elif not p and not q:
            return True
        else:
            return False

    return checkTree(p, q)
