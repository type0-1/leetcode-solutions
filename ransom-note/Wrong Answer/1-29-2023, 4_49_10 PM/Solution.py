// https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        strings = [ransomNote, magazine]
        if strings[0] in strings[1]:
            return True
        return False
        
        
        
