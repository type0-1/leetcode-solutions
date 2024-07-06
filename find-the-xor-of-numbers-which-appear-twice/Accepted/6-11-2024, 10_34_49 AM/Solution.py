// https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        m = set()

        total = 0

        for n in nums:
            if n not in m:
                m.add(n)
            else:
                total = total ^ n
        
        return total