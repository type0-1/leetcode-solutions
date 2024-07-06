// https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I" : 1,
                  "V" : 5,
                  "X" : 10,
                  "L": 50,
                  "C": 100,
                  "D": 500,
                  "M": 1000}
        if len(s) == 1:
            return romans[s[0]]
        s = list(s)
        total = []
        i = 1
        while i < len(s):
            if romans[s[i-1]] < romans[s[i]]:
                if total != []:
                    total.pop(-1)
                total.append(romans[s[i]] - romans[s[i-1]])
            elif i == 1:
                total.append(romans[s[i-1]])
                total.append(romans[s[i]])
            else:
                total.append(romans[s[i]])
            i += 1
        print(total)
        return sum(total)
        

                