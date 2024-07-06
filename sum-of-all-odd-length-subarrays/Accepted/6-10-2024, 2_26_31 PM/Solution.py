// https://leetcode.com/problems/sum-of-all-odd-length-subarrays

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        p1 = 0
        p2 = temp = 1
        total = 0

        while p2 <= len(arr):

            while p2 <= len(arr):
                total += sum(arr[p1:p2])
                p1 += 1
                p2 += 1 
        
            p1 = 0
            p2 = temp + 2
            temp += 2
        
        return total