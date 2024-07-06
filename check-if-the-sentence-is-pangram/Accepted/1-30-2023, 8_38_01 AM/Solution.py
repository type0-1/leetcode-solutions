// https://leetcode.com/problems/check-if-the-sentence-is-pangram

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        a = "abcdefghijklmnopqrstuvwxyz"
        for i in sentence:
            if i in a:
                a = a.replace(i, "", 1)
        if len(a) == 0:
            return True
        return False