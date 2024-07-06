// https://leetcode.com/problems/sort-the-students-by-their-kth-score

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        i = 0
        while i < len(score):
            pos = score[i]
            j = i
            while j < len(score):
                if pos[k] < score[j][k]:
                    tmp = score[i]
                    score[i] = score[j]
                    score[j] = tmp
                j += 1
            i += 1
        return score