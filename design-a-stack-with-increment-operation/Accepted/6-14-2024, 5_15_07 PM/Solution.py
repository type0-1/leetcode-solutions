// https://leetcode.com/problems/design-a-stack-with-increment-operation

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if self.maxSize == len(self.stack):
            return 
        self.stack.append(x)
        

    def pop(self) -> int:
        if self.stack == []:
            return -1
        return self.stack.pop()
        
    def increment(self, k: int, val: int) -> None:
        if len(self.stack) < k:
            self.stack = [n+val for n in self.stack]
        else:
            for i in range(k):
                self.stack[i]+=val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)