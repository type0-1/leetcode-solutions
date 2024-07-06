// https://leetcode.com/problems/find-the-peaks

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:

        result = []

        for i in range(1, len(mountain)-1):
            if mountain[i-1] < mountain[i] and mountain[i] > mountain[i+1]:
                result.append(i)
        
        return result