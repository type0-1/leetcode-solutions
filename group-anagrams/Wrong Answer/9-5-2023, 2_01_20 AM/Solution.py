// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        i = 0
        output = []
        while i < len(strs):
            word = [strs[i]]
            j = i+1
            while j < len(strs):
                if sorted(strs[i]) == sorted(strs[j]):
                    if strs[j] not in word:
                        word.append(strs[j])
                        strs.remove(strs[j])
                j+=1
            i+=1
            output.append(word)
        return output