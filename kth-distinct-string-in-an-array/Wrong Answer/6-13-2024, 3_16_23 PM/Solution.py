// https://leetcode.com/problems/kth-distinct-string-in-an-array

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        print(arr)
        arr = list(set(arr))
        if len(arr) < k:
            return ""
        else:
            print(arr)
            return arr[k]