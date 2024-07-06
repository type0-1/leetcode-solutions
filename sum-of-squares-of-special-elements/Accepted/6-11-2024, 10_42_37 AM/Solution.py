// https://leetcode.com/problems/sum-of-squares-of-special-elements

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        total = 0

        for i in range(len(nums)):
            if not len(nums) % (i+1):
                total += nums[i]**2
        
        return total