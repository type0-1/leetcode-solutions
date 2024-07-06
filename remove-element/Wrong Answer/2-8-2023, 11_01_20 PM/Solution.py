// https://leetcode.com/problems/remove-element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new = [str(n) for n in nums]
        for i in range(len(new)):
            if new[i] == str(val):
                new[i] = "_"
        new.sort()
        return new.count("_")