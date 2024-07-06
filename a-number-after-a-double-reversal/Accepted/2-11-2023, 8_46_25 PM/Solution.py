// https://leetcode.com/problems/a-number-after-a-double-reversal

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num < 10:
            check = str(int(num))[::-1]
            return check[::-1] == str(num)
        else:
            check = str(int(num))[::-1].strip("0")
            return str(num) == check[::-1]
        