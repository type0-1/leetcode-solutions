// https://leetcode.com/problems/missing-number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return [n for n in range(len(nums) + 1) if n not in nums][0]