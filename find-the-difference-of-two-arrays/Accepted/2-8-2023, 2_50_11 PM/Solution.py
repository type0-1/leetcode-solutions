// https://leetcode.com/problems/find-the-difference-of-two-arrays

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        dif1 = []
        dif2 = []
        for n in nums1:
            if n not in nums2 and n not in dif1:
                dif1.append(n)
        for n in nums2:
            if n not in nums1 and n not in dif2:
                dif2.append(n)
        return [dif1, dif2]
