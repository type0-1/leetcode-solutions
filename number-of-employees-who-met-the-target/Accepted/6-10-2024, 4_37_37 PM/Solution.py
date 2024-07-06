// https://leetcode.com/problems/number-of-employees-who-met-the-target

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        hours.sort(reverse=True)
        for n in hours:
            if n >= target:
                count += 1
            else:
                break
        return count