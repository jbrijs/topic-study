# Binary Trees

Binary trees are a non-linear data structure where each node has a value and a reference to a right and left child. The topmost node is called the root, and the bottom most nodes are called leaves.


## Types of Trees

* **Full Binary Tree** - A binary tree where each node has either zero or two child nodes
* **Degenerate Tree** - Each node has only one child (effectively a linked list)
* **Skewed Binary Tree** - A binary tree where each node has children one same direcdtion
* **Complete Binary Tree** - all the levels of the tree are filled completely except for the last level, where it is filled as far to the left as possible
* **Perfect Binary Tree** - Each node except for the leaves have two children
* **Balanced Binary Tree** - The height of the tree is log(N), where N is the number of nodes 
* **Binary Search Tree** - A tree where the each left child is less than the value of its parent, adn the values of the right child is greater than its parent
* **AVL Tree** - A self balancing binary search tree, where the difference between heights of left and right subtrees cannot be more than one
* **Red-Black Tree** - A type of balanced binary search tree which use a sset of rules to maintain balance based on a simple color-coding scheme to adjust the tree after modification
* **B-Tree** - A tree where nodes have a large number of keys, which allows for larger branching and shhhallower height
* **B+ Tree** - Variation of B-Tree, where data pointers are stored only at the leaf nodes of the tree
* **Segment Tree** - A tree that is built recursively by dividing an array into segments until each segment repreents a singl element

## Common Operations

### Traversal

Tree Traversal algorithms can be split into DFS and BFS.

DFS algorithims include:

* **Preorder Traversal** - "Current, left, right". Visit the node, then the left subtree, then the right

* **Inorder Traversal** - "Left, current, right". Visit the left subtree, then the node, then the right subtree

* **Postorder Traverasal** - "Left, right , current". Visit the left subtree, then the right, then the node

BFS is commonly refered to as **Level Order Traversal**

### Insertion

In a standard Binary Tree, node order does not matter. Insertion involves looking at each level for an empty spot. By convention, a node is inserted into the left subtree first if available.

### Searching

Commonly uses a DFS or BFS traversal algorithm until value is found or not

### Deletion

Deletion involves removing a node but preserving the tree structure. First, traverse and find the node to delete. Replace the nodes value with the value of the last node in the tree, and then delete the last node.

***All of these operations are O(N) time, where N is the number of nodes in the tree. To achieve better time complexity, rules are added to the tree( i.e. BST, AVL Tree, B-Tree, etc.).***




