from typing import Optional
from leetcode.trees.invert_tree import TreeNode


"""
Leetcode #449: Serialize and Deserialize BST

Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.
"""


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:

        serialized = []

        def dfs(node):
            if not node:
                serialized.append("null")
            else:
                serialized.append(str(node.val))
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return ",".join(serialized)

    def deserialized(self, data: str) -> Optional[TreeNode]:

        vals = data.split(",")

        def buildTree():
            nonlocal index
            if index == len(vals):
                return None

            val = vals[index]
            index += 1

            if val == "null":
                return None

            node = TreeNode(int(val))

            node.left = buildTree()
            node.right = buildTree()

            return node

        index = 0
        return buildTree()
