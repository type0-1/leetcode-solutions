// https://leetcode.com/problems/goat-latin

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split()
        vowels = "aeiou"
        final = ""
        for i, word in enumerate(sentence):
            if word[0].lower() not in vowels:
                word = word[1:] + word[0] + "ma"
                print(word)
            elif word[0].lower() in vowels:
                word += "ma"
            word += ("a" * (i + 1))
            final += word + " "
        return final.strip()