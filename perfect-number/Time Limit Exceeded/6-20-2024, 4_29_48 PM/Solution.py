// https://leetcode.com/problems/perfect-number

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        total = 0
        for i in range(1, num//2+1):
            if num % i == 0:
                total += i
        return total == num
