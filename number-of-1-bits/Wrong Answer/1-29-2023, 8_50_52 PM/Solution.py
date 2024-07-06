// https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        string = str(n)
        count = 0
        for i in string:
            if i == "1":
                count += 1
        return count