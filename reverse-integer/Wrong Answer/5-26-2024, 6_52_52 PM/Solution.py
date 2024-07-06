// https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        x = int(input())
        n = str(x)
        if n[0] == "-":
            n = int(n[::-1][:-1]) * -1
        else:
            n = int(n[::-1])
        return n
        