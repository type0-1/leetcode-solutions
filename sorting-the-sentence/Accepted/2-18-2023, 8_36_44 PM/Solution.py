// https://leetcode.com/problems/sorting-the-sentence

class Solution:
    def sortSentence(self, s: str) -> str:
       s = s.split()
       words = []
       for word in s:
           word = (word[len(word) - 1], word[:len(word) - 1])
           words.append(word)
       words.sort()
       s = ""
       for word in words:
           s += word[1] + " "
       return s.strip()
           