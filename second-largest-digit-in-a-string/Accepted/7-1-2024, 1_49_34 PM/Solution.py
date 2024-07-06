// https://leetcode.com/problems/second-largest-digit-in-a-string

class Solution:
    def secondHighest(self, s: str) -> int:
        nums = list(set(sorted([int(n) for n in s if n.isnumeric()])))
        if len(nums) <= 1:
            return -1
        else:
            nums.sort(reverse=True)
            return nums[1]