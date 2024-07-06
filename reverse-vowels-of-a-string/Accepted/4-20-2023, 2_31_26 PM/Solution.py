// https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_List = ["a","e","i","o","u", "A", "E", "I", "O", "U"]
        reversedVowels = [vowel for vowel in s if vowel in vowel_List][::-1]
        s = [l for l in s]
        string = ""
        for l in s:
            if l in vowel_List:
                string += reversedVowels.pop(0)
            else:
                string += l
        return string