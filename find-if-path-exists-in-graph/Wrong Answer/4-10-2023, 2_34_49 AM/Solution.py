// https://leetcode.com/problems/find-if-path-exists-in-graph

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.graph = {i : [] for i in range(n)}
        self.visited = [False] * n
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])

        def bfs(source):
            queue = [source]
            self.visited[source] = True
            for node in self.graph[source]:
                if not self.visited[node]:
                    queue.append(node)
                    self.visited[node] = True
                    
        bfs(source)
        if self.visited[source] and self.visited[destination]:
            return True
        return False