// https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        new = "".join(strs)
        string = ""
        subs = []
        for l in strs:
            string += l
            if new.count(string) == len(strs):
                subs.append(string)
                string += l
        print(subs)
