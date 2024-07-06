// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg = []
        for pos in grid:
            for n in pos:
                if n < 0:
                    neg.append(n)
        return len(neg)
