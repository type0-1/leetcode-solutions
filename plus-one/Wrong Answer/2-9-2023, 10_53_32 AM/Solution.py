// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = (digits[-1] + 1)
        s = ""
        new = []
        for i in range(len(digits) - 1):
            s += str(digits[i]) + " "
        for i in s:
            if i.isnumeric():
                new.append(int(i))
        new.append(last)
        ifOne = []
        if len(new) == 1:
            s = str(new[0])
            for i in s:
                ifOne.append(int(i))
            return ifOne
        return new

