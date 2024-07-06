// https://leetcode.com/problems/reverse-words-in-a-string

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word for word in s.strip().split(" ") if len(word) > 0][::-1])