// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        new = ""  
        for l in s:                                                 
            if l not in new:
                new += l
            else:
                if count < len(new):
                    count = len(new)
                else:
                    s = ""
        return count
            
