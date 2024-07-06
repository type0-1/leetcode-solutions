// https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.strip().split()
        zipped = zip(pattern, s)
        check = []
        for pattern in zipped:
            if pattern[0] in check and pattern[1] not in check:
                return False
            else:
                check.append(pattern[0])
                check.append(pattern[1])
        return True
