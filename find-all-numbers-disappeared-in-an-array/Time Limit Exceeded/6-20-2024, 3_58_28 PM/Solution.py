// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        m = []
        nums.sort()
        for i in range(len(nums)):
            if i+1 not in nums:
                m.append(i+1)
        return m