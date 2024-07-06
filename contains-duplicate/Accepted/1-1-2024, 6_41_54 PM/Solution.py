// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        hash_map = {}
        for n in nums:
            if n not in hash_map:
                hash_map[n] = 0
            else:
                return True
        return False
        