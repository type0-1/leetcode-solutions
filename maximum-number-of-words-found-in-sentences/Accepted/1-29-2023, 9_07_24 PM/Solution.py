// https://leetcode.com/problems/maximum-number-of-words-found-in-sentences

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m = 0
        for i in sentences:
            i = i.strip().split()
            if len(i) > m:
                m = len(i)
        return m
