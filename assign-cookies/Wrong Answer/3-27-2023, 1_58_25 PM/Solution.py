// https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        for n in g:
            if n in s:
                count += 1
        return count