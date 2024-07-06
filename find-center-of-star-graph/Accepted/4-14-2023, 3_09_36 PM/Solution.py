// https://leetcode.com/problems/find-center-of-star-graph

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        self.graph = {i : [] for i in range(len(edges) + 2)}

        print(self.graph)
        for i, edge in enumerate(edges):
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])

        for adj in self.graph:
            if len(self.graph[adj]) == len(edges):
                return adj