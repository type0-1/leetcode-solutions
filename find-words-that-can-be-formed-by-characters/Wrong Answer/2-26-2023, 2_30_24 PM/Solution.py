// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0
        for word in words:
            s = word
            for c in s:
                if c in chars:
                    s = s.replace(c, "")
            if len(s) == 0:
                total += len(word)
        return total