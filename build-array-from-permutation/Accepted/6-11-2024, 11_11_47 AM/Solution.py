// https://leetcode.com/problems/build-array-from-permutation

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        new = []

        for i, n in enumerate(nums):
            new.insert(i, nums[nums[i]])
        return new