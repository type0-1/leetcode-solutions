// https://leetcode.com/problems/sort-the-students-by-their-kth-score

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        new = [(sc[k], sc) for sc in score]
        new.sort(reverse=True)
        return [scores[1] for scores in new]