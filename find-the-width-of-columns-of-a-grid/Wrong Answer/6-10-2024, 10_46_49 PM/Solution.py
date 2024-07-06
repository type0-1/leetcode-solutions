// https://leetcode.com/problems/find-the-width-of-columns-of-a-grid

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        
        result = []
        for i in range(len(grid)):
            maximum = 0
            for j in range(len(grid[i])):
                if len(str(grid[i])) > maximum:
                    maximum = len(str(grid[i]))
            result.append(maximum)

        return result