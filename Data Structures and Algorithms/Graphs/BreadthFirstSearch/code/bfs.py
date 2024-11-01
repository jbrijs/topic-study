from collections import deque

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


def bfs(graph, source):
    
    visited = set()
    queue = deque()
    queue.append(source)

    while len(queue) > 0:
        v = queue.popleft()
        if v not in visited:
            visited.add(v)
            for u in graph[v]:
                if u not in visited:
                    queue.append(u)

    return visited


print(f"BFS result: {bfs(graph,0)}")
    


