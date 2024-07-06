// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        get_size = head
        
        while get_size:
            size += 1
            get_size = get_size.next
        
        if size - n <= 0:
            head = None
            return head
        
        i = 0
        temp = head
        
        while i != size-n-1 and temp.next:
            i += 1
            temp = temp.next

        if temp.next is None:
            return head
        else:
            temp.next = temp.next.next 

        return head
