// https://leetcode.com/problems/majority-element-ii

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numbers = [n for n in nums if nums.count(n) > (len(nums) // 3)]
        final = []
        for n in numbers:
            if n not in final:
                final.append(n)
        return final