// https://leetcode.com/problems/minimum-common-value

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        return min([n for n in nums1 if n in nums2])