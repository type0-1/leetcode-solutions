// https://leetcode.com/problems/is-subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        subsequence = sorted([l for l in s if l in t])
        return True if "".join(subsequence) == s else False