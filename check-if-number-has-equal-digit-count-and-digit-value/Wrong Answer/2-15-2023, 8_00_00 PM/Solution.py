// https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value

class Solution:
    def digitCount(self, num: str) -> bool:
        for i in num:
            if num.count(i) != int(i):
                return False
        return True