// https://leetcode.com/problems/design-linked-list

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index > self.length:
            return -1

        node = self.head
        for _ in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)

        if self.head is None:
            self.head = node
            self.tail = node
            self.length += 1
        else:
            node.next = self.head
            self.length += 1
            self.head = node

    def addAtTail(self, val: int) -> None:
        node = Node(val)

        if self.tail is None:
            self.addAtHead(val)
            return

        self.tail.next = node
        node.next = None
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
            curr = self.head

            for _ in range(index):
                prev = curr
                curr = curr.next
            
            prev.next = node
            node.next = curr
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.length:
            return
        elif index == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            node = self.head
            prev = self.head
            for _ in range(index):
                prev = node
                node = node.next
            prev.next = node.next
            self.length -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)