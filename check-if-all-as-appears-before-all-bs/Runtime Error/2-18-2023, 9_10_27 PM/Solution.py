// https://leetcode.com/problems/check-if-all-as-appears-before-all-bs

class Solution:
    def checkString(self, s: str) -> bool:
        i = 0
        a = 0
        b = s.index("b")
        while i < len(s):
            if s[i] == "a":
                a = i
            else:
                b = i
            if a > b:
                return False
            i += 1
        return True
