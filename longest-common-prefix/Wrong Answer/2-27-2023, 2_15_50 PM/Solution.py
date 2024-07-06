// https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        words = [sorted(word) for word in strs]
        s = ""
        prefixes = []
        for word in strs:
            for l in word:
                if all(l in word for word in words):
                    s += l
                elif not all(l in word for word in words):
                    if s not in prefixes and len(s) > 0:
                        prefixes.append(s)
                        s = ""
                    else:
                        s = ""
        if len(prefixes) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            return prefixes[0].strip()
