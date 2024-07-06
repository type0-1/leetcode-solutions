// https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        array = []
        while i < len(matrix):
            if matrix[i][0] < target and matrix[i][len(matrix[i])-1] >= target:
                array = matrix[i]
                break
            i += 1
        
        if target not in array:
            return False
        else:
            return True
        