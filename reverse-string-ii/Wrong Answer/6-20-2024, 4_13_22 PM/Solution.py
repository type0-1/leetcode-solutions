// https://leetcode.com/problems/reverse-string-ii

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if k == 1:
            return s
        if len(s) < k:
            return s[::-1]
        elif len(s) < 2*k and len(s) > k:
            return s[:k][::-1] + s[k:]
        else:
            m = ""
            i = 0
            while i < len(s):
                m += s[i:i+k][::-1]+s[i+k:2*k]
                i += 2*k
            if i-1 == len(s):
                m += s[-1]
            return m