// https://leetcode.com/problems/string-to-integer-atoi

class Solution:
    def myAtoi(self, s: str) -> int:
        nums = int("".join([i for i in s if i.isnumeric() or i == "-"]))
        return nums