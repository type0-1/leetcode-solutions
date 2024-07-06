// https://leetcode.com/problems/counting-bits

class Solution:
    def countBits(self, n: int) -> List[int]:
        new = []
        for i in range(0, n + 1):
            check = bin(i)
            new.append(check.count("1"))
        return new