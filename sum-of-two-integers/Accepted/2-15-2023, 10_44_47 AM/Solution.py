// https://leetcode.com/problems/sum-of-two-integers

class Solution:
    def getSum(self, a: int, b: int) -> int:
        l = []
        l.append(a)
        l.append(b)
        return sum(l)