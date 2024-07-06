// https://leetcode.com/problems/delete-columns-to-make-sorted

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for word in strs:
            sorting = "".join(sorted(word))
            if sorting[::-1] == word:
                count += 1
            elif sorting == word:
                count += 1
            else:
                count -= 1
        return count
            
