// https://leetcode.com/problems/n-repeated-element-in-size-2n-array

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        s = set(nums)
        for n in s:
            if nums.count(n) > 1:
                return n
            