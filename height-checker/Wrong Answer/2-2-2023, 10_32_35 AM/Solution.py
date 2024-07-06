// https://leetcode.com/problems/height-checker

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        heights.sort()
        for i in range(len(heights)):
            if i != heights[i]:
                count += 1
        return count