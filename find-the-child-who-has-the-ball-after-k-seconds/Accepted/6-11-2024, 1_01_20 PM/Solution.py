// https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds

class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        alt = 0
        flag = 0
        m = [i for i in range(n)]
        
        while k != 0:
            if alt == n-1:
                flag = 0
            elif alt == 0:
                flag = 1
            
            if flag == 1:
                alt += 1 
            else:
                alt -= 1
            k -= 1
        return m[alt]