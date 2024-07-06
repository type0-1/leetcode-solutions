// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        hash_set = set()
        for n in nums:
            if n not in hash_set:
                hash_set.add(n)
                return True
        return False
        