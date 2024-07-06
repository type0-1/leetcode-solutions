// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")":"(","]":"[","}":"{"}
        stack = []

        for c in s:
            if c in brackets:
                if len(stack) > 0 and brackets[c] == stack[-1]:
                    stack.pop()
            else:
                stack.append(c)
        
        return stack == []
        