// https://leetcode.com/problems/destination-city

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return paths[-1][-1]
        