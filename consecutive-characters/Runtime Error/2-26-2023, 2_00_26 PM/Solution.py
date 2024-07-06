// https://leetcode.com/problems/consecutive-characters

class Solution:
    def maxPower(self, s: str) -> int:
        counts = []
        count = 0
        previous = s[0]
        for i in range(1, len(s)):
            pos = s[i]
            if pos == previous:
                count += 1
            elif pos != previous:
                counts.append(count)
                count = 0
                previous = pos
        return max(counts) + 1
