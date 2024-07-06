// https://leetcode.com/problems/richest-customer-wealth

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        nums = [sum(account) for account in accounts]
        return max(nums)