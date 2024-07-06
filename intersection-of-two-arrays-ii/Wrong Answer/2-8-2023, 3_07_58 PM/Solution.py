// https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for n in nums1:
            check = (nums1.count(n) > result.count(n) or nums2.count(n) > result.count(n))
            if n in nums2 and check:
                result.append(n)
        return result
