// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:

        x = str(x)

        while len(x) > 1:

            if x[0] != x[-1]:
                return False

            x = x[1:-1]
            
        return True
        