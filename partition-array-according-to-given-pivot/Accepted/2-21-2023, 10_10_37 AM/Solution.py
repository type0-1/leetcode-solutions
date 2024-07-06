// https://leetcode.com/problems/partition-array-according-to-given-pivot

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = [n for n in nums if n < pivot]
        right = [n for n in nums if n > pivot]
        middle = [n for n in nums if n == pivot]
        final = [n for n in left]
        final += [n for n in middle]
        final += [n for n in right]
        return final