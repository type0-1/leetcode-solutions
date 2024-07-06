// https://leetcode.com/problems/occurrences-after-bigram

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split(" ")
        arr = []

        for i in range(1, len(text)):
            if text[i-1] == first and text[i] == second:
                if i+1 != len(text):
                    arr.append(text[i+1])
        
        return arr

