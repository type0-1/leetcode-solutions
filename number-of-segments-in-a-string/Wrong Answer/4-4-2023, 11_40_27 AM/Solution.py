// https://leetcode.com/problems/number-of-segments-in-a-string

class Solution:
    def countSegments(self, s: str) -> int:
        segments = [word for word in s.strip().split() if word[0].isalpha()]
        return len(segments)