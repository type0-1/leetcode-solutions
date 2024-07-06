// https://leetcode.com/problems/squares-of-a-sorted-array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [i ** 2 for i in nums]
        squares.sort()
        return squares