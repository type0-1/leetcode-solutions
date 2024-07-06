// https://leetcode.com/problems/power-of-two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(n):
            if 2 ** i == 0:
                return True
        return False