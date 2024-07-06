// https://leetcode.com/problems/kth-distinct-string-in-an-array

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = 0
        dic = {}
        
        for n in arr:
            if arr.count(n) == 1:
                dic[n] = count
                count += 1
                if count == k:
                    return n
            else:
                continue

        return ""
