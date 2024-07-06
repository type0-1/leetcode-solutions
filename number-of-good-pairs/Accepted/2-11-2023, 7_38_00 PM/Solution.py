// https://leetcode.com/problems/number-of-good-pairs

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = []
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j] and i < j:
                    pairs.append((i, j))
                j += 1
            i += 1
        return len(pairs)