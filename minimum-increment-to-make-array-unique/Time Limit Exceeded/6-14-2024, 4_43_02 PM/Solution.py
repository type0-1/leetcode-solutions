// https://leetcode.com/problems/minimum-increment-to-make-array-unique

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        count = 0
        for i in range(1, len(nums)):
            while nums[i] <= nums[i-1]:
                nums[i] += 1
                count += 1
        return count
