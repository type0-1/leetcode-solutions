// https://leetcode.com/problems/sum-of-squares-of-special-elements

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for i in range(n):
            if not n % (i+1):
                total += nums[i]**2
        
        return total