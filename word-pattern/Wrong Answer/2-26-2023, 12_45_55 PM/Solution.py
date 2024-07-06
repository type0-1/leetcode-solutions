// https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.strip().split()
        zipped = zip(pattern, s)
        check = {}
        for pattern in zipped:
            if pattern[0] not in check:
                check[pattern[0]] = pattern[1]
            elif pattern[0] in check and check[pattern[0]] != pattern[1]:
                return False
        return True