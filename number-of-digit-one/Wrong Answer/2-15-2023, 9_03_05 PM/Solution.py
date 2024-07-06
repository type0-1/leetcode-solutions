// https://leetcode.com/problems/number-of-digit-one

class Solution:
    def countDigitOne(self, n: int) -> int:
        num = str(n)
        count = 0
        if n >= 1 and n <= 9:
            return 1 
        elif n == 0:
            return 0
        else:  
            for i in range(n):
                pos = str(i)
                for n in pos:
                    if n in num:
                        count += 1
            return count