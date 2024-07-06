// https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        
        temp = slow = fast = head

        while fast and fast.next:
            temp = slow 
            slow = slow.next
            fast = fast.next.next
        
        temp.next = None
        prev = None
        curr = slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 
        
        start = head

        while start and prev:
            if start.val != prev.val:
                return False
            start = start.next
            prev = prev.next
        
        return True

    