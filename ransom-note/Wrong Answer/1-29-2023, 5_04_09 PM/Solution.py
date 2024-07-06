// https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = "".join(sorted(ransomNote))
        magazine = "".join(sorted(magazine))
        for i in ransomNote:
            if i in magazine:
                ransomNote = ransomNote.replace(i, "!")
                magazine = magazine.replace(i, "!")
        check = ransomNote.count("!") == magazine.count("!") and ransomNote.count("!") > 0
        if check:
            return True
        return False
