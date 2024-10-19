from leetcode.trees.invert_tree import TreeNode

'''
Leetcode: 235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes 
p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''


def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

    def getAncestors(node, find, ancestors):
        ancestors.append(node)

        if node.val == find.val:
            return ancestors

        elif node.val > find.val:
            return getAncestors(node.left, find, ancestors)
        else:
            return getAncestors(node.right, find, ancestors)

    p_stack = getAncestors(root, p, [])
    q_stack = getAncestors(root, q, [])

    while len(p_stack) > 0 and len(q_stack) > 0:
        if p_stack[-1] == q_stack[-1]:
            return p_stack[-1]
        else:
            if len(p_stack) > len(q_stack):
                p_stack.pop()
            elif len(p_stack) < len(q_stack):
                q_stack.pop()
            else:
                p_stack.pop()
                q_stack.pop()
