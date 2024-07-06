// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new = []
        for n in nums:
            if n not in new:
                new.append(n)
        left = len(nums) - len(new)
        new.sort()
        for i in range(left):
            new.append("_")
        return new 