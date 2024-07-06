// https://leetcode.com/problems/majority-element-ii

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) < 3:
            if nums.count(nums[0]) == len(nums):
                return [nums[0]]
            else:
                return nums
        else:
            nums.sort()
            return [nums[len(nums) // 3]]