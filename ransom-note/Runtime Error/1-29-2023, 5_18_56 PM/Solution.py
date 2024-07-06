// https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        i = 0
        count = 0
        while i < len(ransomNote):
            if ransomNote[i] in magazine:
                ransomNote = ransomNote.replace(ransomNote[i], "", 1)
                magazine = magazine.replace(ransomNote[i], "", 1)
                count += 1
            i += 1
        check = len(magazine) - len(ransomNote)
        if check > 0 and check == count:
            return True
        else:
            return False
