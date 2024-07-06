// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums2 = set(nums)
        for n in nums2:
            if nums.count(n) > 1:
                return True
        return False