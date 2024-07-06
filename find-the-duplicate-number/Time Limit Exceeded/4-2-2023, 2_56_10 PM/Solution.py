// https://leetcode.com/problems/find-the-duplicate-number

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_set = set(nums)
        for n in num_set:
            if nums.count(n) > 1:
                return n 