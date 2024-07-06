// https://leetcode.com/problems/maximum-sum-with-exactly-k-elements

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        total = 0
        ind = nums.index(max(nums))
        for i in range(k):
            total += nums[ind]
            nums[ind] += 1
        return total