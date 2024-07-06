// https://leetcode.com/problems/middle-of-the-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        length = 0

        while curr != None:
            length += 1
            curr = curr.next

        mid = 0

        if length % 2 == 0:
            mid = (length // 2)
        else:
            mid = length // 2
        
        pos = 0 
        curr = head

        while pos != mid:
            curr = curr.next
            pos += 1
        
        return curr



        