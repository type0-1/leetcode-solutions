// https://leetcode.com/problems/find-the-n-th-value-after-k-seconds

class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        l = [1] * n
        for i in range(k):
            for j in range(len(l)):
                l[j] = sum(l[:j])
        
        return l[-1] % 10**9+7
    