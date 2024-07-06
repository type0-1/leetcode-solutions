// https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for n in nums1:
            if n in nums2:
                check = min(nums1.count(n), nums2.count(n))
                if result.count(n) < check:
                    result.append(n)
        return result