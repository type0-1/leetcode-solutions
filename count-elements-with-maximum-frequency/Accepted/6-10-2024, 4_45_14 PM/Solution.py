// https://leetcode.com/problems/count-elements-with-maximum-frequency

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = {}
        
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1 
        
        values = sorted([v for v in dic.values()], reverse=True)
        total = 0
        m = values[0]

        for i in range(len(values)):
            if values[i] == m:
                total += m
            else:
                break
        
        return total
        