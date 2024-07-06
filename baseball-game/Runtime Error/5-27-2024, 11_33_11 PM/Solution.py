// https://leetcode.com/problems/baseball-game

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for c in operations:
            if c.isnumeric():
                record.append(c)
            elif c == "+":
                record.append(record.pop(-1) + record.pop(-1))
            elif c == "D":
                record.append(record[-1]*2)
            else:
                record.pop(-1)
        return sum(record)
        