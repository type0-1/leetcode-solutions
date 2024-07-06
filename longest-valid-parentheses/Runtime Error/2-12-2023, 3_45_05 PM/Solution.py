// https://leetcode.com/problems/longest-valid-parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        count = 0
        if len(s) <= 1:
            return count
        else:  
            for i in range(len(s)):
                if s[i] == "(" and s[i + 1] == ")":
                    count += 2
                else:
                    pass
        return count
