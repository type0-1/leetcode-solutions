// https://leetcode.com/problems/sort-even-and-odd-indices-independently

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        e = []
        o = []

        result = []

        for n in nums:
            if n % 2:
                o.append(n)
            else:
                e.append(n)
        
        e.sort()
        o.sort(reverse=True)

        while e and o:
            result.append(e.pop(0))
            result.append(o.pop(0))
        
        if e:
            return result + e
        elif o:
            return result + o
        return result