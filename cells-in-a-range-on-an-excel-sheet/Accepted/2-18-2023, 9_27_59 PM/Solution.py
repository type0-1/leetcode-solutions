// https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        new = []
        s = s.split(":")
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(alpha.index(s[0][0]), alpha.index(s[1][0]) + 1):
            for j in range(int(s[0][1:]), int(s[1][1:]) + 1):
                  new.append(alpha[i] + str(j))
                  j += 1
            i += 1
        return new