// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return None
        
        forward = head

        for i in range(n):
            forward = forward.next
        
        curr = head
        prev = None

        while forward:
            prev = curr
            curr = curr.next
            forward = forward.next
        
        prev.next = curr.next
        return head
    

        
        