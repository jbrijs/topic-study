from typing import Optional

from leetcode.trees.invert_tree import TreeNode


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    max_diameter = [0]
    if root == None:
        return 0

    def findHeight(root):
        if root == None:
            return 0

        left_height = findHeight(root.left)
        right_height = findHeight(root.right)

        max_diameter[0] = max(max_diameter[0], left_height + right_height)

        return 1 + max(left_height, right_height)

    findHeight(root)
    return max_diameter[0]
