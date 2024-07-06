// https://leetcode.com/problems/max-consecutive-ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        numbers = []
        total = 0
        for n in nums:
            if n == 1:
                total += 1
            elif n != 1:
                numbers.append(total)
                total = 0
        numbers.append(total)
        return max(numbers)
            