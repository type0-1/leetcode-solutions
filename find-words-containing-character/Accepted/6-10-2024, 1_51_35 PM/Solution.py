// https://leetcode.com/problems/find-words-containing-character

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        array = []
        for i, word in enumerate(words):
            if x in word:
                array.append(i)
        
        return array