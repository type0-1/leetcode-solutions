// https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums) / 2
        return [n for n in nums if nums.count(n) > size][0]