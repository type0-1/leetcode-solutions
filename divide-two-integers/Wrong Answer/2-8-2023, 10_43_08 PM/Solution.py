// https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648:
            return 2147483647
        return int(dividend / divisor)