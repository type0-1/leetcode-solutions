// https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = 0
        for c in ransomNote:
            if c in magazine:
                ransomNote = ransomNote.replace(c, "!")
                magazine = magazine.replace(c, "!")
        check = ransomNote.count("!") == magazine.count("!") and ransomNote.count("!") > 0
        if check:
            return True
        else:
            return False
        
