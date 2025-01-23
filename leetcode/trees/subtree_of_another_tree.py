"""
Leetcode #572: Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
"""

from leetcode.trees.invert_tree import TreeNode
from typing import Optional


def isSubTree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

    def isSameTree(node, subnode):

        if not node and not subnode:
            return True

        if not node or not subnode:
            return False

        return (
            (node.val == subnode.val)
            and isSameTree(node.right, subnode.right)
            and isSameTree(node.left, subnode.left)
        )

    if not root:
        return False

    if isSameTree(root, subRoot):
        return True

    return isSubTree(root.left, subRoot) or isSubTree(root.right, subRoot)
