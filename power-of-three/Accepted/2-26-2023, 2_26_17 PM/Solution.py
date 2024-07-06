// https://leetcode.com/problems/power-of-three

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(n + 1):
           power = 3 ** i
           if power > n:
               return False
           else:
               if power == n:
                   return True