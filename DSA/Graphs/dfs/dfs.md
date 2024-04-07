# Depth First Search


Depth first search is a graph traversal algorithm. It starts by exploring a node and adding it to the stack. Then it explores its neigbhor and adds that node to the stack. Once it hits a dead end, it will pop the first node of the stack and explore its remaining neighbors. It utilizes a data structure, usually an array of length n (n representing nodes in the graph G) to keep track of which nodes have been visited. To avoid getting stuck in a cycle, a node will not be pushed to the stack if it has already been visited. 

DFS can also be implemented recursively, replacing our defined stack with the call stack which keeps track of which vertex to explore.

