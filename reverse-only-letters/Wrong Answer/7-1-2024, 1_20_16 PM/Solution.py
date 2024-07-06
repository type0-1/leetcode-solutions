// https://leetcode.com/problems/reverse-only-letters

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        lets = [c for c in s if c.isalpha()][::-1]
        chars = [(c, i) for i, c in enumerate(s) if not c.isalpha()]

        s = ""

        for i in range(len(lets)):
            if len(chars) == 0:
                s += lets[i]
            elif i == chars[0][1]:
                s += chars.pop(0)[0]
                s += lets[i]

        return s