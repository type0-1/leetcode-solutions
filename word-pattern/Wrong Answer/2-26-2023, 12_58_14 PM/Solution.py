// https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.strip().split()
        zipped = zip(pattern, s)
        check = [(l, word) for l, word in zipped]
        for i in range(len(check)):
            pos = check[i]
            for j in range(i + 1, len(check)):
                pos2 = check[j]
                if pos[0] == pos2[0] and pos[1] != pos2[1]:
                    return False
                elif pos[0] != pos2[0] and pos[1] == pos2[1]:
                    return False
        return True