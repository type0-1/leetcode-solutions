// https://leetcode.com/problems/apply-operations-to-an-array

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                nums[i-1]*=2
                nums[i] = 0#
        numbers = [n for n in nums if n != 0]
        zeros = [n for n in nums if n == 0]
        return numbers + zeros