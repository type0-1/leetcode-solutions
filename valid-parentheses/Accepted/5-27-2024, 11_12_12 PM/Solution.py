// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        dic = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c not in dic:
                brackets.append(c)
            else:
                try:
                    if brackets.pop() != dic[c]:
                        return False
                except:
                    return False
                    
        if len(brackets) > 0:
            return False
        return True
