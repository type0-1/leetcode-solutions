// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for n in nums:
            if n not in seen:
                seen.append(n)
            else:
                return False
        return True