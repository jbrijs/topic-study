package BreadthFirstSearch.code;

import java.util.ArrayDeque;
import java.util.Queue;

public class BFS {
    /* The graph is a directed graph represented as an adjacency matrix */

    public static int [][] graph = {
   
        {0, 1, 1, 0, 1},  /// Node 0 has edges to nodes 1, 2, and 4
        {1, 0, 1, 0, 0},  ///Node 1 has edges to nodes 0 and 2
        {0, 1, 0, 1, 1},  /// Node 2 has edges to nodes 1, 3, and 4
        {1, 0, 0, 0, 1},  /// Node 3 has edges to nodes 0 and 4
        {0, 1, 1, 1, 0} /// Node 4 has edges to nodes 1, 2, and 3
    };

    public boolean[] bfs(int[][]graph, int source){
        
        boolean[] visited = new boolean[graph.length];
        Queue<Integer> queue = new ArrayDeque<>();
        queue.offer(source);
        visited[source] = true;

        while (!queue.isEmpty()){
           int v = queue.poll();
           for (Integer u: graph[v]) {
                if (!visited[u]) { 
                    queue.offer(u);
                    visited[u] = true;
                }
           }
        }
        

        return visited;
    }
}
