// https://leetcode.com/problems/n-repeated-element-in-size-2n-array

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        dic = {}
        
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                return n