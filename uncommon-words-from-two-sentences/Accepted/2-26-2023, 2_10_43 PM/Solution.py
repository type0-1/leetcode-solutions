// https://leetcode.com/problems/uncommon-words-from-two-sentences

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.strip().split()
        s2 = s2.strip().split()
        uncommons1 = [word for word in s1 if word not in s2 and s1.count(word) == 1]
        uncommons2 = [word for word in s2 if word not in s1 and s2.count(word) == 1]
        both = (" ".join(uncommons1) + " " +  " ".join(uncommons2)).split(" ")
        final = [word for word in both if len(word) > 0]
        return final
