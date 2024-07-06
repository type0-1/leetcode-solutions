// https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        i = 0
        n = nums[0]
        count = 0

        while i < len(nums):
            if n == nums[i]:
                count += 1
            if count >= 2:
                count = 0
                n = nums[i+1]
            i += 1
        
        return n