// https://leetcode.com/problems/row-with-maximum-ones

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        count = 0
        pos = 0
        
        for i in range(len(mat)):
            if count < mat[i].count(1):
                count = mat[i].count(1)
                pos = i
        
        return [pos, count]