// https://leetcode.com/problems/unique-number-of-occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        m = set(arr)
        seen = set()
        for n in m:
            if arr.count(n) not in seen:
                seen.add(arr.count(n))
            else:
                return False
        return True
