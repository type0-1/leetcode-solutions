// https://leetcode.com/problems/merge-sorted-array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        if 0 not in nums1:
            return nums1
        for i in range(nums1.index(0), len(nums1)):
            nums1[i] = nums2.pop(0)

        nums1.sort()
        