// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new = []
        for n in nums:
            if n not in new:
                new.append(n)
        return len(new)