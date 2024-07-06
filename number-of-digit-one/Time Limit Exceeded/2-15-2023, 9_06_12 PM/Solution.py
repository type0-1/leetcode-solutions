// https://leetcode.com/problems/number-of-digit-one

class Solution:
    def countDigitOne(self, n: int) -> int:
        num = str(n)
        if n >= 1 and n <= 9:
            return 1 
        elif n == 0:
            return 0
        else:  
            nums = []
            for i in range(n + 1):
                pos = str(i)
                if pos.count("1") > 0:
                    nums.append(pos.count("1"))
            return sum(nums)