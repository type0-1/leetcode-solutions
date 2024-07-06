// https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        else:
            nums = [[1],[1,1]]
            for i in range(2, numRows):
                arr = [1]
                for j in range(1,len(nums[-1])):
                    arr.append(nums[-1][j]+nums[-1][j-1])
                arr.append(1)
                nums.append(arr)
            return nums
        