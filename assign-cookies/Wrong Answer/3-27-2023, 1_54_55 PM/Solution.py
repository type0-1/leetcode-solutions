// https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        dic = {}
        for n in g:
            if n in s:
                dic[n] = 1
        return len(dic)