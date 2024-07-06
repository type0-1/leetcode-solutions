// https://leetcode.com/problems/clear-digits

class Solution:
    def clearDigits(self, s: str) -> str:
        m = []

        for i in range(len(s)):
            if s[i].isalpha():
                m.append(s[i])
            else:
                m.pop()
        return "".join(m)