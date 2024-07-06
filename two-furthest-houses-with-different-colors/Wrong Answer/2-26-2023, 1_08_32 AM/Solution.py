// https://leetcode.com/problems/two-furthest-houses-with-different-colors

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        distance = 0
        for index, house in enumerate(colors):
            if colors[0] != house:
                distance = index
        return distance