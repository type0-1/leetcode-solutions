// https://leetcode.com/problems/median-of-two-sorted-arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        if len(nums1) % 2 == 0:
            print(nums1)
            return (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2
        print(nums1)
        return nums1[len(nums1) // 2]
       