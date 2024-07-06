// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        s2 = ""

        pos1 = l1
        pos2 = l2

        while pos1:
            s1 += str(pos1.val)
            pos1 = pos1.next
        
        while pos2:
            s2 += str(pos2.val)
            pos2 = pos2.next

        result = str(int(s1[::-1]) + int(s2[::-1]))[::-1]

        final = ListNode()
        head = final

        for i in range(len(result) - 1):
            final.val = int(result[i])
            final.next = ListNode()
            final = final.next
            
        final.val = int(result[-1])
        return head