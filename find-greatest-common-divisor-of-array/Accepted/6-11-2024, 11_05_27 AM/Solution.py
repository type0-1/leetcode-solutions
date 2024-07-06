// https://leetcode.com/problems/find-greatest-common-divisor-of-array

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        gcd = 0
        mini, maxi = min(nums), max(nums)

        for i in range(1, maxi+1):
            if mini%i == 0 and maxi%i == 0:
                gcd = i
        return gcd