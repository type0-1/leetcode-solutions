// https://leetcode.com/problems/maximum-69-number

class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        try:
            m = s.index("6")
            s = list(s)
            s[m] = "9"
            return int("".join(s))
        except:
            return int(s)