// https://leetcode.com/problems/find-all-duplicates-in-an-array

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for n in nums:
            if nums.count(n) > 1 and n not in result:
                result.append(n)
        return result
