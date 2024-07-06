// https://leetcode.com/problems/count-common-words-with-one-occurrence

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count = 0
        for word in words1:
            if word in words2 and (words1.count(word) == words2.count(word)):
                count += 1
        return count