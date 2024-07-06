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
        print(len(subs))
        if len(max(subs)) > 1:
            return max(subs)
        else:
            return ""
