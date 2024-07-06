// https://leetcode.com/problems/camelcase-matching

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ups = []
        count = 0
        new = ""
        for s in pattern:
            if s.isupper() and count < 1:
                count += 1
                new += s
            elif s.isupper() and count == 1:
                count = 0
                ups.append(new)
                new = ""
            else:
                new += s
        print(ups)
                
