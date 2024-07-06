// https://leetcode.com/problems/sort-array-by-parity

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []

        for n in nums:
            if n % 2:
                odd.append(n)
            else:
                even.append(n)
        
        return even + odd