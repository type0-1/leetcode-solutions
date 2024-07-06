// https://leetcode.com/problems/create-target-array-in-the-given-order

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        zipped = zip(index, nums)
        for element in zipped:
            result.insert(element[0], element[1])
        return result