// https://leetcode.com/problems/goal-parser-interpretation

class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("()", "o")
        for l in command:
            if l == "(" or l == ")":
                command = command.replace(l, "")
        return command