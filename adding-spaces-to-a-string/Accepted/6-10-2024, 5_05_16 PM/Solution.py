// https://leetcode.com/problems/adding-spaces-to-a-string

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        string = ""
        for i, st in enumerate(s):
            if spaces and spaces[0] == i:
                spaces.pop(0)
                string += " "
            string += st
        return string
        