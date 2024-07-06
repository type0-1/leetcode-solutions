// https://leetcode.com/problems/left-and-right-sum-differences

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        array1 = []
        array2 = []
        array3 = []

        for i in range(len(nums)):
            array1.append(sum(nums[:i]))
            array2.append(sum(nums[len(nums)-i:]))
        
        array2 = array2[::-1]

        for i in range(len(array1)):
            array3.append(abs(array1[i]-array2[i]))
        return array3