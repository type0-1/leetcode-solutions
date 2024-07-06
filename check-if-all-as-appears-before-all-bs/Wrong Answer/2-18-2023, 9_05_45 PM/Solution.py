// https://leetcode.com/problems/check-if-all-as-appears-before-all-bs

class Solution:
    def checkString(self, s: str) -> bool:
        aLoop = 0
        bLoop = 0
        i = 0
        while i < len(s):
            if s[i] == "b":
                bLoop = i
            elif s[i] == "a":
                aLoop = i
            if aLoop > 0 and bLoop > 0 and aLoop > bLoop:
                return False
            i += 1
        return True