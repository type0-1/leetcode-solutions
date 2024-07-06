// https://leetcode.com/problems/camelcase-matching

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ups = []
        count = 0
        s = ""
        for i in pattern:
            if i.isupper() and count < 1:
                s += i
                count += 1
            elif i.islower():
                s += i
            elif i.isupper and count == 1:
                ups.append(s)
                s = ""
                count = 0
            print(s)
        print(ups)
