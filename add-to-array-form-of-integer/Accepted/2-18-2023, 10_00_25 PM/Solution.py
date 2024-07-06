// https://leetcode.com/problems/add-to-array-form-of-integer

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        new = int("".join([str(n) for n in num]))
        result = str(new + k)
        return [int(n) for n in result]