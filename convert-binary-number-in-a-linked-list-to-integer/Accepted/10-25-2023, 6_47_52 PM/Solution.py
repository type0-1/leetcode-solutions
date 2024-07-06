// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        curr = head
        length = -1

        while curr != None:
            curr = curr.next
            length += 1

        curr = head
        total = 0

        while curr != None:
            total += (curr.val * (2 ** length))
            curr = curr.next
            length -= 1
        
        return total
        