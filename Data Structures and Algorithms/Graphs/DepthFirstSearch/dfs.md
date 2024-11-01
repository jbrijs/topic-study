# Depth First Search (DFS)

## Description

Depth First Search (DFS) is a graph traversal algorithm that explores as far as possible along each branch before backtracking. It starts by exploring a node `v` and adding it to the stack. Then it explores an unvisited neighbor `u` of `v` and adds `u` to the stack. The algorithm continues exploring unvisited neighbors, going as "deep" as possible. When it reaches a dead end (a node with no unvisited neighbors), it pops the top node off the stack and backtracks to explore other paths. This process continues until the stack is empty, indicating that all reachable nodes have been visited.

DFS typically uses a stack to keep track of nodes whose neighbors still need to be explored and another data structure, usually a set or array, to keep track of visited nodes. This prevents the algorithm from revisiting nodes.

DFS can also be implemented recursively, using the call stack to keep track of the vertices to explore. This approach replaces the explicit use of a stack data structure with the implicit call stack.


### Common Use Cases

Depth First Search (DFS) is a versatile algorithm that can be used in various scenarios, including:

1. **Path Finding:** DFS can be used to determine if there is a path between two nodes in a graph. It can also be used to find all possible paths between two nodes.

2. **Detecting Cycles:** DFS can be used to detect cycles in a graph, which is useful for checking if a graph is a Directed Acyclic Graph (DAG) or for identifying cycles in undirected graphs.

3. **Topological Sorting:** In a directed graph, DFS can be used to perform topological sorting, which is useful for scheduling tasks, resolving dependencies, and other applications where the order of operations is important.

4. **Connected Components:** In an undirected graph, DFS can be used to find all connected components, which can be useful for network analysis, clustering, and other applications.

5. **Solving Puzzles and Mazes:** DFS can be used to solve puzzles such as mazes or the n-queens problem by exploring different configurations and backtracking when necessary.

Other graph traversal algorithms that implement DFS include:

- **Tarjan's Algorithm:** Used for finding strongly connected components in a directed graph.
- **Kosaraju's Algorithm:** Another algorithm for finding strongly connected components.
- **Bridges and Articulation Points:** DFS can be used to find bridges (edges whose removal increases the number of connected components) and articulation points (nodes whose removal increases the number of connected components) in a graph.
- **Backtracking Algorithms:** Many backtracking algorithms, such as those used for solving combinatorial problems, are based on DFS principles.



