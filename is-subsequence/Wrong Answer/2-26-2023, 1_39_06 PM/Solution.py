// https://leetcode.com/problems/is-subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        new = ""
        for l in t:
            if l in s:
                new += l
        return new == s
