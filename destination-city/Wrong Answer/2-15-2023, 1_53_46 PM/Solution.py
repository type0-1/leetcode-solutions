// https://leetcode.com/problems/destination-city

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        new = [path for path in paths]
        return new[-1][1]