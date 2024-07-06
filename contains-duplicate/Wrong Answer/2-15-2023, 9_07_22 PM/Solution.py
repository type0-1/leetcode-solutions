// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for n in nums:
            if nums.count(n) > 0:
                return False
        return True