// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or n == 0 or head.next is None:
            return None
            
        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next
        
        i = 0
        node = head

        while i+1 != length-n:
            node = node.next
            i += 1

        node.next = node.next.next
        return head


        
        