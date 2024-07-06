// https://leetcode.com/problems/power-of-four

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(n + 1):
           power = 4 ** i
           if power > n:
               return False
           else:
               if power == n:
                   return True