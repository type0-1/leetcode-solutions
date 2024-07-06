// https://leetcode.com/problems/distribute-elements-into-two-arrays-i

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n1, n2 = [], []

        n1.append(nums.pop(0))
        n2.append(nums.pop(0))

        for n in nums:
            if n1[-1] > n2[-1]:
                n1.append(n)
            else:
                n2.append(n)

        return n1 + n2 