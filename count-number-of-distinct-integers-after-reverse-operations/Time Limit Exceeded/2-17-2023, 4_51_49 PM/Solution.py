// https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        new = []
        for n in nums:
            new.append(n)
        for i in range(len(nums)):
            s = str(nums[i])
            new.append(int(s[::-1]))
        final = []
        for n in new:
            if n not in final:
                final.append(n)
        return len(final)