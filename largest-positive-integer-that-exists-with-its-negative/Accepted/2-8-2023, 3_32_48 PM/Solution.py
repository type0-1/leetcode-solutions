// https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        big = [n for n in nums if n < 0 and abs(n) in nums]
        if len(big) == 0:
            return -1 
        else:
            n = abs(min(big))
            return n
