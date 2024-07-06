// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        other = list(set(nums))
        print(other)
        k = len(other)
        nums = other + (["_"] * (len(nums) - len(other))) 
        return k