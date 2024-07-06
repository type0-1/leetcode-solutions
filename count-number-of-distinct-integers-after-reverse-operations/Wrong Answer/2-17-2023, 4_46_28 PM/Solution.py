// https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            s = str(nums[i])
            nums.append(int(s[::-1]))
        for n in nums:
            if nums.count(n) == 1:
                count += 1
        return count