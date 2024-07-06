// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = ""
        for c in s:
            if c.isalpha():
                pal += c.lower()
            elif c.isnumeric():
                pal += c
        if pal == pal[::-1]:
            return True
        return False