// https://leetcode.com/problems/sum-of-unique-elements

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum([n for n in nums if nums.count(n) == 1])