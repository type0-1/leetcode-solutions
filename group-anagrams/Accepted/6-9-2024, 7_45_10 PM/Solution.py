// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for word in strs:
            sorted_str = "".join(sorted(word))

            if sorted_str not in seen:
                seen[sorted_str] = [word]
            else:
                seen[sorted_str].append(word)
        
        return [word_list for word_list in seen.values()]