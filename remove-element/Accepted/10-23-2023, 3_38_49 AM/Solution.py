// https://leetcode.com/problems/remove-element

class Solution:

    def removeElement(self, nums: list[int], val: int) -> int:

        one = []
        two = []
        count = 0

        for n in nums:
            if n == val:
                two.append("_")
            else:
                one.append(n)
                count += 1

        one += two
        for i in range(len(nums)):
            nums[i] = one[i]
            
        return count    
