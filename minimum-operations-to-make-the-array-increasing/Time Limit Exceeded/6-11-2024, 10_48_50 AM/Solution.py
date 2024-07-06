// https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        n = len(nums)
        count = 0
        for i in range(1, n):
            while nums[i-1] >= nums[i]:
                nums[i] += 1
                count += 1
        return count