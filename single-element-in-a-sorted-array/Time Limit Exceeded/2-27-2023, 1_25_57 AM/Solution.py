// https://leetcode.com/problems/single-element-in-a-sorted-array

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return [n for n in nums if nums.count(n) == 1][0]