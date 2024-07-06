// https://leetcode.com/problems/set-mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        final = []
        for i, n in enumerate(nums):
            if nums.count(n) > 1:
                final.append(i + 1)
        return final 

