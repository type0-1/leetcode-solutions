// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")":"(","]":"[","}":"{"}
        stack = []
        flag = 0
        if len(s) <= 1 or s[0] in brackets:
            return False 

        for c in s:
            if c in brackets:
                if len(stack) > 0 and brackets[c] == stack[-1]:
                    stack.pop()
                else:
                    flag = 1
            else:
                stack.append(c)

        return stack == [] and flag == 0