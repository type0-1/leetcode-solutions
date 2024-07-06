// https://leetcode.com/problems/set-mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = {}
        nums.sort()
        for i, n in enumerate(nums):
            if n not in seen:
                seen[n] = i+1
            else:
                return [seen[n], i+1]