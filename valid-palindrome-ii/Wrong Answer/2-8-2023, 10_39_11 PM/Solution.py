// https://leetcode.com/problems/valid-palindrome-ii

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s[0].lower() == s[-1].lower():
            return True
        elif s.lower() == s[::-1].lower():
            return True
        return False