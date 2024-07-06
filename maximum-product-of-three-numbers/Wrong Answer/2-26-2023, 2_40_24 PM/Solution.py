// https://leetcode.com/problems/maximum-product-of-three-numbers

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        total = 1
        for i in range(3):
            total *= nums[i]
        return total
