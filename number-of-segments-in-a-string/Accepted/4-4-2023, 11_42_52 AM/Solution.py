// https://leetcode.com/problems/number-of-segments-in-a-string

class Solution:
    def countSegments(self, s: str) -> int:
        s = s.split()
        count = 0
        for element in s:
            if element != " ":
                count += 1
        return count