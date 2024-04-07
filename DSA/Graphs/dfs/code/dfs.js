/* Graph is represented as a dictionay of adjacency lists */

const graph = {
  0: [1, 2, 4], // Node 0 has edges to nodes 1, 2, and 4
  1: [0, 2], // Node 1 has edges to nodes 0 and 2
  2: [1, 3, 4], // Node 2 has edges to nodes 1, 3, and 4
  3: [0, 4], // Node 3 has edges to nodes 0 and 4
  4: [1, 2, 3], // Node 4 has edges to nodes 1, 2, and 3
};

function dfs(graph, source) {
  const visited = new Set();
  const stack = [source];

  while (stack.length > 0) {
    v = stack.pop();
    if (!visited.has(v)) {
      visited.add(v);
      graph[v].forEach((u) => {
        stack.push(u);
      });
    }
  }
  return visited
}


console.log(dfs(graph, 0))