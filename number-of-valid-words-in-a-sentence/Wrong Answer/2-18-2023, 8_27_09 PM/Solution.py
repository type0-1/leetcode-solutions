// https://leetcode.com/problems/number-of-valid-words-in-a-sentence

class Solution:
    def countValidWords(self, sentence: str) -> int:
        sentence = sentence.split()
        count = 0
        for word in sentence:
            if word.isalpha():
                count += 1
        return count