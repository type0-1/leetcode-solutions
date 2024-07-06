// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        dic = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c not in dic:
                brackets.append(c)
            else:
                if brackets.pop() != dic[c]:
                    return False
        return True
