// https://leetcode.com/problems/ugly-number

class Solution:
    def isUgly(self, n: int) -> bool:
        nums = [2,3,5]
        return (n // 2) in nums
        