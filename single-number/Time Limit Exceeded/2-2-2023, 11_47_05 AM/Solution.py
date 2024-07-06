// https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = [str(number) for number in nums]
        for i in num:
            if num.count(i) == 1:
                return int(i)