// https://leetcode.com/problems/most-frequent-even-element

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        numbers = [n for n in nums if n % 2 == 0]
        numbers.sort()
        print(numbers[0])