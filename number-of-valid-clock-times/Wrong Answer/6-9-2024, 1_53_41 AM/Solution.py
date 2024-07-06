// https://leetcode.com/problems/number-of-valid-clock-times

class Solution:
    def countTime(self, time: str) -> int:
        time = list(time)
        time.pop(2)
        
        valid = 1

        if time[0] == "?":
            valid *= 2
        if time[1] == "?" and time[0] == "?":
            valid *= 12
        elif time[1] == "?" and time[0] is not "?":
            valid *= 10
        if time[2] == "?":
            valid *= 6
        if time[3] == "?":
            valid *= 10
        if valid == 1:
            valid = 0
        
        return valid