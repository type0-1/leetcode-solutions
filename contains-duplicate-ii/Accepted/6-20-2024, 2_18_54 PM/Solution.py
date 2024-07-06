// https://leetcode.com/problems/contains-duplicate-ii

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, n in enumerate(nums):
            if n not in seen:
                seen[n] = [i]
            else:
                for ind in seen[n]:
                    if abs(ind-i) <= k:
                        return True
                seen[n].append(i)
                
        return False