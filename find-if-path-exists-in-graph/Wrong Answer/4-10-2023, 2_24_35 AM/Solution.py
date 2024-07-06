// https://leetcode.com/problems/find-if-path-exists-in-graph

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.graph = {i : [] for i in range(n)}
        self.visited = [False] * n
        self.marked = [-1] * n
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
        def dfs(vertex):
           self.visited[vertex] = True
           for node in self.graph[vertex]:
               if not self.visited[node]:
                   self.marked[node] = vertex
                   dfs(node)
        dfs(source)
        print(self.marked, self.visited)
        def hasPathTo(vertex):
            return self.visited[vertex]
        
        def pathTo(vertex):
            if not hasPathTo(vertex):
                return []
            
            path = [vertex]
            print(path)
        
        print(pathTo(source))



