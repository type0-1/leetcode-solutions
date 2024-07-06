// https://leetcode.com/problems/reverse-string-ii

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            return s[::-1]
        elif len(s) < 2*k and len(s) > k:
            return s[:k][::-1] + s[k:]
        else:
            m = ""
            for i in range(0, len(s), 2*k):
                m += s[i:i+k][::-1]+s[i+k:2*k]
            if len(s)%2:
                return m+s[-1]
            else:
                return m