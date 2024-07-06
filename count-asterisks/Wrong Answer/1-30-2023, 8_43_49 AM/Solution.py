// https://leetcode.com/problems/count-asterisks

class Solution:
    def countAsterisks(self, s: str) -> int:
        s = s.split("|")
        m = 0
        for i in s:
            if i.count("*") > m:
                m = i.count("*")
        return m
