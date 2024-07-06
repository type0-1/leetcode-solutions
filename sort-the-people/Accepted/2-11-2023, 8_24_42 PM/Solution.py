// https://leetcode.com/problems/sort-the-people

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zipped = zip(names, heights)
        sorting = [(num, name) for name, num in zipped]
        sorting.sort(reverse=True)
        result = [data[1] for data in sorting]
        return result
            
