// https://leetcode.com/problems/majority-element-ii

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numbers = [n for n in nums if nums.count(n) > (len(nums) // 3)]
        for i, n in enumerate(numbers):
            if numbers.count(n) > 1:
                numbers.pop(i)
        return numbers