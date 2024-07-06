// https://leetcode.com/problems/valid-perfect-square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return str(num**0.5)[-2] == "." and str(num**0.5)[-1] == "0"