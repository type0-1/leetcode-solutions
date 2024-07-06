// https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case

class Solution:
    def greatestLetter(self, s: str) -> str:
        letters = []

        for c in s:
            if c.upper() in s and c.lower() in s:
                letters.append(c.upper())

        letters.sort(reverse=True)
        if letters == []:
            return ""
        return letters[0]