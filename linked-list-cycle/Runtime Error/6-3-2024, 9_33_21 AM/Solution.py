// https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if pos == -1:
            return False
            
        slow = fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow.val == fast.val:
                return True
        
        return False