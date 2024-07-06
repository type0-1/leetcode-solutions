// https://leetcode.com/problems/sum-of-all-odd-length-subarrays

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int: 
        result = [n for n in arr]
        result.append(sum(arr))
        count = 3
        for i in range(len(arr)):
            pos = arr[i:count]
            if len(pos) == 3:
                result.append(pos)
            else:
                break
            count += 1
        total = 0
        for n in result:
            if type(n) == int:
                total += n
            elif type(n) == list:
                for i in n:
                    total += i
        return total