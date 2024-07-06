// https://leetcode.com/problems/divisible-and-non-divisible-sums-difference

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        first = sum([x for x in range(1,n+1) if not x%m])
        second = sum([x for x in range(1,n+1) if x%m])

        return second - first