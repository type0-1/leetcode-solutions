// https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        new = []
        count = 0
        for n in nums:
            new.append(n)
        for i in range(len(nums)):
            s = str(nums[i])
            new.append(int(s[::-1]))
        for n in new:
            if new.count(n) == 1:
                count += 1
        return count