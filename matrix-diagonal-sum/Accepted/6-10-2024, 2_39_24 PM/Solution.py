// https://leetcode.com/problems/matrix-diagonal-sum

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0

        for i in range(len(mat)):
            if len(mat)%2 and i == len(mat)-i-1:
                total += mat[i][i]
                continue
            total += mat[i][i]
            total += mat[len(mat)-i-1][i]
        
        return total 