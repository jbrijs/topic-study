from typing import Optional
from leetcode.trees.invert_tree import TreeNode

'''
Leetcode #230 Kth Smallest Element in a BST
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
'''


def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inOrderTraversal(node):
            if not node:
                return []

            return inOrderTraversal(node.left) + [node.val] + inOrderTraversal(node.right)

        in_order = inOrderTraversal(root)

        return in_order[k - 1]