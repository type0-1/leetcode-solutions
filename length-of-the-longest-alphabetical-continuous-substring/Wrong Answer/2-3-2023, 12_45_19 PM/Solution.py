// https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        new = ""
        count = 0
        for i in s:
            if i not in new:
                new += i
                count += 1
            else:
                break
        return count

