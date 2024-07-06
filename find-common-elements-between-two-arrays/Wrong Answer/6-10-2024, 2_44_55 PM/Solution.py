// https://leetcode.com/problems/find-common-elements-between-two-arrays

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans1 = ans2 = 0

        for i, n in enumerate(nums1):
            if n in nums1:
                ans1 += 1
        
        for i, n in enumerate(nums2):
            if n in nums2:
                ans2 += 1
        
        return [ans1, ans2]