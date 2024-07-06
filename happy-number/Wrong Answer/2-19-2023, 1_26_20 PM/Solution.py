// https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        check = str(n)
        while int(check) > 9:
            total = 0
            check = str(check)
            for i in check:
                total += int(i) ** 2
            check = total
        if check == 1:
            return True
        return False
                
