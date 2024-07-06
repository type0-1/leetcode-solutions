// https://leetcode.com/problems/is-subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        new = ""
        if len(t) == 0:
            return False
        elif len(t) == 0 and len(s) == 0:
            return True
        for l in t:
            for l2 in s:
                if l == l2:
                    new += l2
                    break
        return new == s or new == t