// https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        new = "".join(strs)
        string = ""
        subs = []
        if len(strs) == 0:
            return ""
        for l in new:
            if new.count(string) == len(strs):
                subs.append(string)
                string += l
            else:
                string = ""
                string += l
        if len(max(subs)) > 1:
            return max(subs)
        return ""
