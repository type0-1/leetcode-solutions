// https://leetcode.com/problems/maximum-product-difference-between-two-pairs

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        shortest = nums[:2]
        biggest = nums[len(nums) - 2:]
        short = shortest[0] * shortest[1]
        big = biggest[0] * biggest[1]
        return big - short
