// https://leetcode.com/problems/find-center-of-star-graph

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        s = ""
        for l in edges:
            for i in l:
                s += str(i)
                print(s)
        for i in s:
            if s.count(i) == len(edges):
                return int(i)