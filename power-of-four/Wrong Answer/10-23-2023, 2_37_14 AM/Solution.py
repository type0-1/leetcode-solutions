// https://leetcode.com/problems/power-of-four

import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            n = -n
        if len(str(math.log(n, 4))[2:]) == 1:
            return True
        return False
        