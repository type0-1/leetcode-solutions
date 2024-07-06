// https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        biggest = 0
        for n in nums:
            if n < 0 and abs(n) in nums and abs(n) > biggest:
                biggest = abs(n)
        if biggest = 0:
            return -1
        return biggest

