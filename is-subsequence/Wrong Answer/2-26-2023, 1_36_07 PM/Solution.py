// https://leetcode.com/problems/is-subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for l in s:
            if l in t:
                s = s.replace(l, "")
        return len(s) == 0