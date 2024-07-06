// https://leetcode.com/problems/smallest-number-in-infinite-set

class SmallestInfiniteSet:

    def __init__(self):
        self.ifs = [i for i in range(1, 1001)]
        

    def popSmallest(self) -> int:
        if self.ifs != []:
            return self.ifs.pop(self.ifs.index(min(self.ifs)))

        

    def addBack(self, num: int) -> None:
        if num not in self.ifs:
            self.ifs.append(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)