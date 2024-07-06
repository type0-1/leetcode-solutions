// https://leetcode.com/problems/is-subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        subsequence = [l for l in t if l in s]
        if "".join(subsequence) in s:
            return True
        elif len(subsequence) == 0:
            return False
        else:
            return "".join(subsequence) == s