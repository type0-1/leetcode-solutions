// https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        new = "".join(strs)
        string = ""
        subs = []
        for l in new:
            if new.count(string) == len(strs):
                subs.append(string)
                string += l
            else:
                string = ""
                string += l
        if len(subs) > 1 and len(max(subs)) > 1:
            return max(subs)
        else:
            return ""
