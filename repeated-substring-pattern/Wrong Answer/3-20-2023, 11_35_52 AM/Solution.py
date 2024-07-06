// https://leetcode.com/problems/repeated-substring-pattern

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return True
        else:
            sub= s[0:2]
            for i, l in enumerate(s):
                if s.count(sub) > 1:
                    return True
                else:
                    sub += l
        return False


                 