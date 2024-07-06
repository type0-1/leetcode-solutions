// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stringD = "".join(str(n) for n in digits)
        stringD = str(int(stringD) + 1)
        return [int(n) for n in stringD]