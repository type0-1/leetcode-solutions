// https://leetcode.com/problems/merge-sorted-array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        if 0 not in nums1:
            return nums1

        i = nums1.index(0)
        while i < len(nums1) and len(nums2) != 0:
            nums1[i] = nums2.pop(0)
            i += 1

        nums1.sort()
        