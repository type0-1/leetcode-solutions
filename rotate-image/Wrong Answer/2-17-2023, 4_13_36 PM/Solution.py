// https://leetcode.com/problems/rotate-image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        new = []
        count = 0
        for i in range(len(matrix)):
            pos = []
            for j in range(len(matrix[i])):
                pos.append(matrix[j][count])
            count += 1
            new.append(pos[::-1])
        self.matrix = new
        """
        Do not return anything, modify matrix in-place instead.
        """