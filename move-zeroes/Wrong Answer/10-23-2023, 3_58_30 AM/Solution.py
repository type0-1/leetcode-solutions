// https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.append(nums.pop(i))
        """
        Do not return anything, modify nums in-place instead.
        """
        