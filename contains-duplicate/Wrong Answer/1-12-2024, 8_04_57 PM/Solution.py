// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        hash_set = set()
        for n in nums:
            if n in hash_set:
                return False
            hash_set.add(n)
        return True
        