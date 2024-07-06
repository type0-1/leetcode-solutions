// https://leetcode.com/problems/count-tested-devices-after-test-operations

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        count = 0
        for i, bat in enumerate(batteryPercentages):
            if bat > 0:
                count += 1
                for j in range(i+1, len(batteryPercentages)):
                    batteryPercentages[j] = max(0, batteryPercentages[j]-1)
        return count