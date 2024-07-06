// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")":"(","]":"[","}":"{"}
        stack = []

        if len(s) <= 1 or s[0] in brackets:
            return False 

        for c in s:
            if c in brackets:
                if len(stack) > 0 and brackets[c] == stack[-1]:
                    stack.pop()
            else:
                stack.append(c)

        return stack == []