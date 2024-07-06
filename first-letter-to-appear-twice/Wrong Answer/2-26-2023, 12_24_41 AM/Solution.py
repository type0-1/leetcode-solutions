// https://leetcode.com/problems/first-letter-to-appear-twice

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        s = ""
        for l in s:
            s += l
            if s.count(l) == 2:
                return l