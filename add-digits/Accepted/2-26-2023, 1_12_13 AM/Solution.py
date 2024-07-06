// https://leetcode.com/problems/add-digits

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            string = str(num)
            total = 0
            for n in string:
                total += int(n)
            num = total
        return num