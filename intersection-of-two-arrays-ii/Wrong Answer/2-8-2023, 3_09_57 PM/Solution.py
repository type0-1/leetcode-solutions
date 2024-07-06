// https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for n in nums1:
            if n in nums2:
                if result.count(n) <= nums1.count(n):
                    result.append(n)
                elif result.count(n) <= nums1.count(n):
                    result.append(n)
        return result
