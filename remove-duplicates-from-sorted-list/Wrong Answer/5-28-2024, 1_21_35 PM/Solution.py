// https://leetcode.com/problems/remove-duplicates-from-sorted-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        prev = head
        curr = head.next

        while curr:
            if curr.val == prev.val:
                prev.next = curr.next
            prev = curr
            curr = curr.next
        
        if head is not None and head.next is not None:
            prev = head 
            curr = head.next
            while curr:
                if curr.val == prev.val and curr.next is not None:
                    prev.next = curr.next
                prev = curr
                curr = curr.next
            
        return head