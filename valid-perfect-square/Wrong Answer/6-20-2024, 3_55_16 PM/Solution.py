// https://leetcode.com/problems/valid-perfect-square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return len(str(num**0.5)) == 3 and str(num**0.5)[-1] == "0"