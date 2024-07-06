// https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = [n for n in nums if n < 0]
        pos = [n for n in nums if n > 0]
        if len(neg) > len(pos):
            return len(neg)
        return len(pos)