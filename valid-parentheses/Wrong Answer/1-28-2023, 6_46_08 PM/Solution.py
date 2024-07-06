// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        chars = ["()", "{}", "[]"]
        checks = []
        i = 1
        while i < len(s):
            pos = s[i - 1:i + 1]
            checks.append(pos)
            i += 2
        check = 0
        for i in checks:
            if i in chars:
                check = 1
            else:
                check = 0
        if check == 0:
            return False
        else:
            return True