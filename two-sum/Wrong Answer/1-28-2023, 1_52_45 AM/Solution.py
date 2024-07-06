// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums):
            result = target - nums[i]
            if result in nums:
                print(nums[i])
            i += 1
