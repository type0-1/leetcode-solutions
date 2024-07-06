// https://leetcode.com/problems/separate-the-digits-in-an-array

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        array = []
        for n in nums:
            for c in str(n):
                array.append(int(c))
        return array