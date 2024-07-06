// https://leetcode.com/problems/shuffle-string

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        if indices == sorted(indices):
            return s
        
        array = []

        for i in range(len(s)):
            array.append((indices[i], s[i]))
        
        array.sort()

        s = ""
        for i in range(len(array)):
            s += array[i][1]
        
        return s