// https://leetcode.com/problems/remove-linked-list-elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        while head.val != val:
            head = head.next
        
        curr = head

        while curr != None:
            if curr.next != None and curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next
        return head
        