// https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        n = str(x)

        if n[0] == "-":
            n = int(n[::-1][:-1]) * -1
        else:
            n = int(n[::-1])
        
        if x > 2**31 or x < -(2**31):
            return 0
            
        return n
        