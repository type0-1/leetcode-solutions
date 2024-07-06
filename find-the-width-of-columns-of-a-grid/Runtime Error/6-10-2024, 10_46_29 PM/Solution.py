// https://leetcode.com/problems/find-the-width-of-columns-of-a-grid

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        
        result = []
        for i in range(len(matrix)):
            maximum = 0
            for j in range(len(matrix[i])):
                if len(str(matrix[i])) > maximum:
                    maximum = len(str(matrix[i]))
            result.append(maximum)

        return result