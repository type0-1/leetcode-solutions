// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        string = str(n)
        t1 = 0
        for i in string:
            t1 += int(i)
        t2 = 1
        for i in string:
            t2 *= int(i)
        return t2 - t1
