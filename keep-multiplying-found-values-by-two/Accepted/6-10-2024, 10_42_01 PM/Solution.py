// https://leetcode.com/problems/keep-multiplying-found-values-by-two

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        if original not in nums:
            return original
        
        n = nums[nums.index(original)]*2

        while n in nums:
            n *= 2
        
        return n
            