// https://leetcode.com/problems/percentage-of-letter-in-string

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return s.count(letter) / len(s) * 100