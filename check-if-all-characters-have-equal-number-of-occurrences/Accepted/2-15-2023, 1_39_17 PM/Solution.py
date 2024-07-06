// https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = s.count(s[0])
        i = 0
        for i in s:
            if s.count(i) != count:
                return False
        return True
                