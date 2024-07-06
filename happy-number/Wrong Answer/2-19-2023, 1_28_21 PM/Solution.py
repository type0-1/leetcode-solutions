// https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        while n > 9:
            total = 0
            n = str(n)
            for i in n:
                total += int(i) ** 2
            n = total
        if n == 1:
            return True
        return False
                
