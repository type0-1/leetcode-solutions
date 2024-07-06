// https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = 0
        for c in ransomNote:
            if c in magazine:
                ransomNote = ransomNote.replace(c, "", 1)
                magazine = magazine.replace(c, "", 1)
                count += 1
        if len(ransomNote) == 0:
            return True
        return False