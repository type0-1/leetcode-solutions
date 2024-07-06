// https://leetcode.com/problems/linked-list-random-node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head 
        

    def getRandom(self) -> int:
        length = 0

        temp = self.head
        while temp:
            length += 1
            temp = temp.next
        
        node = self.head
        for _ in range(random.randint(0, length-1)):
            node = node.next
        
        return node.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()