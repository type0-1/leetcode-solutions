// https://leetcode.com/problems/third-maximum-number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        new = []
        for n in nums:
            if n not in new:
                new.append(n)
        if len(new) <= 2:
            return max(new)
        else:
            return new[2]