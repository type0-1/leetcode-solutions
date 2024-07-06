// https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        st = ""
        for w in words:
            st += w[0]
        return st == s