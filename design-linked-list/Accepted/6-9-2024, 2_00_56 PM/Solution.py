// https://leetcode.com/problems/design-linked-list

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        node = self.head
        for _ in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head)
        self.head = node
        if self.length == 0:
            self.tail = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            node = Node(val)
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            node.next = prev.next
            prev.next = node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
            if self.length == 1:
                self.tail = None
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            prev.next = prev.next.next
            if index == self.length - 1:
                self.tail = prev
        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
