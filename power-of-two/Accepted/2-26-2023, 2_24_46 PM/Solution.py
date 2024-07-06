// https://leetcode.com/problems/power-of-two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(n + 1):
           power = 2 ** i
           if power > n:
               return False
           else:
               if power == n:
                   return True