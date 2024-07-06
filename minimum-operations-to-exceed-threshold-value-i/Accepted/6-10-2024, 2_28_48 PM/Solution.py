// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        for n in nums:
            if n < k:
                count += 1
        return count