// https://leetcode.com/problems/maximum-value-of-a-string-in-an-array

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        biggest = 0
        for data in strs:
            if data.isnumeric():
                if int(data) > biggest:
                    biggest = int(data)
            elif data.isalnum():
                if len(data) > biggest:
                    biggest = len(data)
        return biggest