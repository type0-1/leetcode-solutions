// https://leetcode.com/problems/decompress-run-length-encoded-list

class Solution(object):
    def decompressRLElist(self, nums):
        array = []
        for i in range(1, len(nums), 2):
            array += [nums[i]] * nums[i-1]
        return array