// https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        totalElement = 0
        for n in nums:
            totalElement += n
        totalDigit = 0
        s = ""
        for i in nums:
            s += str(i)
        for i in s:
            totalDigit += int(i)
        return totalElement - totalDigit