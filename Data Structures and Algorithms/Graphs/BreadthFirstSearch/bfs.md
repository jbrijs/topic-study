# Breadth First Search (BFS)

## Description

Breadth First Search (BFS) is a graph traversal algorithm that explores all the neighbors of a node before moving on to the neighbors of those neighbors. It starts by exploring a node `v` and then explores all of `v`'s unvisited neighbors `u`. Each unvisited neighbor is added to a FIFO (First In, First Out) queue. Once all neighbors of `v` have been explored, a node is dequeued, and its neighbors are explored next. This process continues until there are no more nodes in the queue. The term "breadth" refers to the algorithm's strategy of exploring all paths one step away from the current node before moving on to paths two steps away, and so on.

BFS typically uses a FIFO queue to keep track of the nodes to explore next. It also uses an array or set to keep track of which nodes have already been visited to ensure that each node is visited only once.

## Common Use Cases

Breadth First Search (BFS) is commonly used in various scenarios, including:

1. **Shortest Path:** BFS can be used to find the shortest path between two nodes in an unweighted graph. The first path found by BFS is guaranteed to be the shortest.
2. **Connected Components:** In an undirected graph, BFS can be used to find all connected components.
3. **Level Order Traversal:** In tree or graph data structures, BFS is used for level order traversal, where nodes are visited level by level.
4. **Cycle Detection:** BFS can be used to detect cycles in an undirected graph.
5. **Network Broadcasting:** BFS is used in networking for broadcasting information from one node to all other nodes in a network.
6. **Puzzle Solving:** BFS is used to solve puzzles such as the sliding tile puzzle or the Knight's tour problem by exploring all possible states one move away, then all states two moves away, and so on.
