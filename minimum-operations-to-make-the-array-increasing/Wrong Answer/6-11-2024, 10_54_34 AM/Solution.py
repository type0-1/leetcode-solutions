// https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        n = len(nums)
        count = 0

        for i in range(1, n):
            if nums[i-1] >= nums[i]:
                nums[i] = nums[i]+(nums[i-1]-nums[i])+1
                count += nums[i]+(nums[i-1]-nums[i])+1
            print(nums)
        return count-nums[-2]