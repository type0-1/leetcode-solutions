// https://leetcode.com/problems/count-odd-numbers-in-an-interval-range

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return len([i for i in range(low, high + 1) if i % 2 != 0])