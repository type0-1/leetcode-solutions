// https://leetcode.com/problems/count-prefixes-of-a-given-string

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for word in words:
            if word[0] == s[0]:
                for c in word:
                    if c not in word:
                        continue
                count += 1
        return count