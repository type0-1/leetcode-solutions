// https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split()
        nums = [int(n) for n in s if n.isnumeric()]
        i = 1
        while i < len(nums):
            if not nums[i - 1] < nums[i]:
                return False
            i += 1
        return True