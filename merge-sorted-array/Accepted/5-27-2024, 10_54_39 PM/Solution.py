// https://leetcode.com/problems/merge-sorted-array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        if nums2 == [] or 0 not in nums1:
            return nums1
        
        i = 0
        while i < len(nums1) and len(nums2) != 0:
            if nums1[i] == 0:
                nums1[i] = nums2.pop(0)
            i += 1

        nums1.sort()