// https://leetcode.com/problems/baseball-game

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for c in operations:
            if c.isnumeric():
                record.append(int(c))
            elif c == "+":
                record.append(record[-2] + record[-1])
            elif c == "D":
                record.append(record[-1] * 2)
            elif c == "C":
                record.pop(-1)
        return sum(record)
        