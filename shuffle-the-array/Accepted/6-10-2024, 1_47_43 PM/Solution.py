// https://leetcode.com/problems/shuffle-the-array

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        if len(nums) == 1:
            return nums

        i = 0
        new = []

        while i < len(nums)//2:
            new.append(nums[i])
            new.append(nums[i+n])
            i += 1
        
        return new