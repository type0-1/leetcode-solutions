// https://leetcode.com/problems/neither-minimum-nor-maximum

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1
        return sorted(nums)[1]