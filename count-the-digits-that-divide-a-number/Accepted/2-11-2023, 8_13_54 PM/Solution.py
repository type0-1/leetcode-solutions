// https://leetcode.com/problems/count-the-digits-that-divide-a-number

class Solution:
    def countDigits(self, num: int) -> int:
        if num < 10:
            return 1
        else:
            n = str(num)
            count = 0
            for i in n:
                if num % int(i) == 0:
                    count += 1
            return count