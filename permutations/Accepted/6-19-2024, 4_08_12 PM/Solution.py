// https://leetcode.com/problems/permutations

from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = permutations(nums)

        return [list(p) for p in list(perm)]