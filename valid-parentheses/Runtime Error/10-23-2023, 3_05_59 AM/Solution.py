// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")":"(","]":"[","}":"{"}
        stack = []
        
        if len(s) <= 1:
            return False

        for c in s:
            if c in brackets:
                if brackets[c] == stack[-1] and stack != []:
                    stack.pop()
            else:
                stack.append(c)
                
        return stack == []
        