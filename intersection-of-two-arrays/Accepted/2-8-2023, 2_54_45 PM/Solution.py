// https://leetcode.com/problems/intersection-of-two-arrays

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for n in nums1:
            if n in nums2 and result.count(n) == 0:
                result.append(n)
        return result