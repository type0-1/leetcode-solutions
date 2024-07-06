// https://leetcode.com/problems/linked-list-cycle-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None 
        
        i = 0
        node = head
        dic = {}

        while node:
            if node in dic:
                return node
            else:
                dic[node] = True
            i += 1
            node = node.next
        
        return node

        