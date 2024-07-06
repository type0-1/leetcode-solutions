// https://leetcode.com/problems/power-of-four

import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n == 1:
            return True

        total = 1

        while total < n:
            total *= 4
            if total == n:
                return True

        return False

        