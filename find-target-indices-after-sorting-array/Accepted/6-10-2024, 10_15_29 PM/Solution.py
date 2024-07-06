// https://leetcode.com/problems/find-target-indices-after-sorting-array

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        dic = {}

        for i, n in enumerate(nums):
            if n not in dic:
                dic[n] = [i]
            else:
                dic[n].append(i)
        
        if target not in dic:
            return []
        return dic[target]