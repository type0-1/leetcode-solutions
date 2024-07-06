// https://leetcode.com/problems/reverse-prefix-of-word

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s = ""
        for i in range(len(word)):
            if word[i] == ch:
                s += word[:i + 1]
                s = s[::-1]
                s += word[i + 1:]
                break
        if len(s) == 0:
            return word
        return s