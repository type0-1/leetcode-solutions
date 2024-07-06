// https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = round(dividend/divisor)
        return result