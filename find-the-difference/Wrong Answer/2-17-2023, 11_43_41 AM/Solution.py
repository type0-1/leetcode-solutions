// https://leetcode.com/problems/find-the-difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for l in s:
            if l in t:
                t = t.replace(l, "")
                s = s.replace(l, "")
        return t
