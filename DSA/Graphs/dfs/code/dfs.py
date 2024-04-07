
'''
The graph is represented as adjacency lists stored in a dictionary. It is a directed graph.
'''

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}



def dfs(graph, source):
    
    visited = set()
    stack = [source] #Add the source node to the stack

    while stack:
        v = stack.pop() 
        if v not in visited: #If v has not been visited, 
            visited.add(v)
            for u in graph[v]:
                if u not in visited:
                    stack.append(u)
    
    return visited #Returns the set of all visited nodes in the graph


print(dfs(graph, 0))