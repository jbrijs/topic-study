package DepthFirstSearch.code;

import java.util.ArrayDeque;
import java.util.Deque;

/* The graph is a directed graph represented as an adjacency matrix */

/**
 * dfs
 */
public class DFS {

    public static int [][] graph = {
   
        {0, 1, 1, 0, 1},  /// Node 0 has edges to nodes 1, 2, and 4
        {1, 0, 1, 0, 0},  ///Node 1 has edges to nodes 0 and 2
        {0, 1, 0, 1, 1},  /// Node 2 has edges to nodes 1, 3, and 4
        {1, 0, 0, 0, 1},  /// Node 3 has edges to nodes 0 and 4
        {0, 1, 1, 1, 0} /// Node 4 has edges to nodes 1, 2, and 3
    };

    public static boolean[] dfs(int[][] graph, int source){
        
        boolean[] visited = new boolean[graph.length];
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(source);

        while (stack.peek() != null){
            int v = stack.pop();
            if (!visited[v]){
                visited[v] = true;
                for (int u = 0; u < graph[v].length; u++) {
                    if (graph[v][u] == 1 && !visited[u]) {
                        stack.push(u);
                    }
                }
            }
        }
        return visited;
    }

    public static boolean[] dfsRecursive(int[][] graph, int source, boolean[] visited){
        if (!visited[source]){
            visited[source] = true;
            for (int u = 0; u < graph[source].length; u++){
                if (graph[source][u] == 1 && !visited[u]){
                    dfsRecursive(graph, u, visited);
                }
            }
        }
        return visited;
    }

    public static void main(String[] args) {
        boolean[] dfsRes = dfs(graph, 0);

        boolean[] visited = new boolean[graph.length];
        boolean[] dfsRecRes = dfsRecursive(graph, 0, visited);

        System.out.print("DFS iterative: ");
        for (boolean value: dfsRes){
            System.out.printf("%s, ",value);
        }
        System.out.println();

        System.out.print("DFS recursive: ");
        for (boolean value: dfsRecRes){
            System.out.printf("%s, ",value);
        }

       
    }
    
}


