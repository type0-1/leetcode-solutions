// https://leetcode.com/problems/repeated-substring-pattern

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sub = ""
        if len(s) == 1:
            return False
        elif len(s) == 2:
            return False if s.counts[0] > 1 else True
        else:
            sub = s[0:2]
            for i, l in enumerate(s):
                if s.count(sub) > 1:
                    return True
                else:
                    sub += l
        return False



                 