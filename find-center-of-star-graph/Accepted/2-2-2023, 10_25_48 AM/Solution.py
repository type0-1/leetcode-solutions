// https://leetcode.com/problems/find-center-of-star-graph

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        s = ""
        for l in edges:
            for i in l:
                s += str(i) + " "
        s = s.split()
        for i in s:
            if s.count(i) > 1:
                return int(i)