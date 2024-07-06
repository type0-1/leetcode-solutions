// https://leetcode.com/problems/delete-greatest-value-in-each-row

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        total = 0
        for i in range(len(grid)):
            total += grid.pop(grid[i].index(max(grid[i])))
        return total