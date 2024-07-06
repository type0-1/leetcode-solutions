// https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        m = len(nums)

        for i in range(m):
            if nums[i] == 0:
                nums.append(nums.pop(i))
                i -= 1
            