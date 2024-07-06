// https://leetcode.com/problems/third-maximum-number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        if len(nums) == 2:
            return nums[:-1]
        elif len(nums) == 1:
            return nums[0]
        else:
            return nums[2]