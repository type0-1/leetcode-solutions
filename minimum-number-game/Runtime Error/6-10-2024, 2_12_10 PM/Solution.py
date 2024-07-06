// https://leetcode.com/problems/minimum-number-game

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        alice = 0
        bob = 0
        
        while nums != []:
            alice = nums.pop(min(nums))
            bob = nums.pop(min(nums))

            arr.append(bob)
            arr.append(alice)
        
        return arr