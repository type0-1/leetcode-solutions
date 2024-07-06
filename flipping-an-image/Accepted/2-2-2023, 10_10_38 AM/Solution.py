// https://leetcode.com/problems/flipping-an-image

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        new = [l[::-1] for l in image]
        for sets in new:
            for i in range(0, len(sets)):
                if sets[i] == 1:
                    sets[i] = 0
                else:
                    sets[i] = 1
        return new